import copy

from datasource.repository.game_repository import GameRepository

from domain.model.board import Board
from domain.model.current_game import CurrentGame
from domain.model.game_status import GameStatus

from domain.service.game_service import GameService

EMPTY = 0


class GameServiceImpl(GameService):

    def __init__(
        self,
        repository: GameRepository,
    ):
        self._repository = repository

    def create_game(
        self,
        player_id: str,
        with_computer: bool,
    ) -> CurrentGame:

        game = CurrentGame()

        game.player1_id = player_id

        game.current_player_id = player_id

        if with_computer:

            game.player2_id = "computer"

        else:

            game.player2_id = None

        if game.player2_id is not None:

            game.status = GameStatus.PLAYER_TURN

        else:

            game.status = GameStatus.WAITING_FOR_PLAYER

        self._repository.save(game)

        return game

    def get_available_games(
        self,
    ) -> list[CurrentGame]:

        return self._repository.find_waiting_games()

    def join_game(
        self,
        game_id: str,
        player_id: str,
    ) -> CurrentGame:

        game = self._repository.get(game_id)

        if game is None:

            raise Exception("Game not found")

        if game.player2_id is not None:

            raise Exception("Game already started")

        game.player2_id = player_id

        game.status = GameStatus.PLAYER_TURN

        self._repository.save(game)

        return game

    def get_game(
        self,
        game_id: str,
    ) -> CurrentGame | None:

        return self._repository.get(game_id)

    def make_move(
        self,
        current_game: CurrentGame,
        player_id: str,
        row: int,
        column: int,
    ) -> CurrentGame:

        if self.is_game_finished(current_game):

            raise Exception("Game already finished")

        if current_game.current_player_id != player_id:

            raise Exception("Not your turn")

        if current_game.board.cells[row][column] != EMPTY:

            raise Exception("Cell already occupied")

        symbol = self._get_player_symbol(
            current_game,
            player_id,
        )

        current_game.board.cells[row][column] = symbol

        winner = self._check_winner(current_game.board)

        if winner is not None:

            current_game.status = GameStatus.PLAYER_WON

            current_game.winner_id = player_id

        elif self._is_board_full(current_game.board):

            current_game.status = GameStatus.DRAW

        else:

            current_game.current_player_id = self._get_next_player(
                current_game,
                player_id,
            )

        self._repository.save(current_game)

        return current_game

    def make_computer_move(
        self,
        current_game: CurrentGame,
    ) -> CurrentGame:

        if current_game.player2_id != "computer":

            return current_game

        if self.is_game_finished(current_game):

            return current_game

        move = self._find_best_move(current_game.board)

        if move is None:

            return current_game

        row, column = move

        current_game.board.cells[row][column] = current_game.player2_symbol

        winner = self._check_winner(current_game.board)

        if winner is not None:

            current_game.status = GameStatus.PLAYER_WON

            current_game.winner_id = current_game.player2_id

        elif self._is_board_full(current_game.board):

            current_game.status = GameStatus.DRAW

        else:

            current_game.current_player_id = current_game.player1_id

        self._repository.save(current_game)

        return current_game

    def validate_board(
        self,
        current_game: CurrentGame,
    ) -> bool:

        cells = [cell for row in current_game.board.cells for cell in row]

        return all(cell in (0, 1, 2) for cell in cells)

    def is_game_finished(
        self,
        current_game: CurrentGame,
    ) -> bool:

        return current_game.status in (
            GameStatus.DRAW,
            GameStatus.PLAYER_WON,
        )

    def _get_player_symbol(
        self,
        game: CurrentGame,
        player_id: str,
    ) -> int:

        if game.player1_id == player_id:

            return game.player1_symbol

        if game.player2_id == player_id:

            return game.player2_symbol

        raise Exception("Player not found")

    def _get_next_player(
        self,
        game: CurrentGame,
        current_player: str,
    ) -> str:

        if game.player1_id == current_player:

            return game.player2_id

        return game.player1_id

    def _check_winner(
        self,
        board: Board,
    ):

        cells = board.cells

        lines = list(cells)

        lines.extend([[cells[row][column] for row in range(3)] for column in range(3)])

        lines.append([cells[i][i] for i in range(3)])

        lines.append([cells[i][2 - i] for i in range(3)])

        for line in lines:

            if line[0] != EMPTY and line[0] == line[1] and line[1] == line[2]:

                return line[0]

        return None

    def _is_board_full(
        self,
        board: Board,
    ) -> bool:

        return all(cell != EMPTY for row in board.cells for cell in row)

    def _find_best_move(
        self,
        board: Board,
    ):

        best_score = -999

        best_move = None

        for row in range(3):

            for column in range(3):

                if board.cells[row][column] == EMPTY:

                    board_copy = copy.deepcopy(board)

                    board_copy.cells[row][column] = 2

                    score = self._minimax(
                        board_copy,
                        False,
                    )

                    if score > best_score:

                        best_score = score

                        best_move = (
                            row,
                            column,
                        )

        return best_move

    def _minimax(
        self,
        board: Board,
        is_maximizing: bool,
    ):

        winner = self._check_winner(board)

        if winner == 2:

            return 10

        if winner == 1:

            return -10

        if self._is_board_full(board):

            return 0

        if is_maximizing:

            best_score = -999

            for row in range(3):

                for column in range(3):

                    if board.cells[row][column] == EMPTY:

                        board.cells[row][column] = 2

                        score = self._minimax(
                            board,
                            False,
                        )

                        board.cells[row][column] = EMPTY

                        best_score = max(
                            best_score,
                            score,
                        )

            return best_score

        else:

            best_score = 999

            for row in range(3):

                for column in range(3):

                    if board.cells[row][column] == EMPTY:

                        board.cells[row][column] = 1

                        score = self._minimax(
                            board,
                            True,
                        )

                        board.cells[row][column] = EMPTY

                        best_score = min(
                            best_score,
                            score,
                        )

            return best_score
