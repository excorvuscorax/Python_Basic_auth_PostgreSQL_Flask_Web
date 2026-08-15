### Task 1. Adding a Database

- Define the connection to a PostgreSQL database using SQLAlchemy.
- Remove the storage class.
- Add appropriate annotations to class parameters that need to be persisted in the database.

### Task 2. Adding Authorization

- Add users with UUID, login, and password.
- Implement user support across all layers.
- Create a SignUpRequest model containing login and password.
- Create an authorization service that uses UserService:
  - a registration method that accepts a SignUpRequest and returns a success status;
  - an authorization method that accepts login and password encoded in Base64 (login:password) in the header and returns the user’s UUID.
- Create an authorization controller with the following endpoints:
  - user registration;
  - user authorization (login).
- Create a UserAuthenticator structure that protects against requests from unauthorized users:
  - validate login and password;
  - if validation succeeds, process the request;
  - if validation fails, respond with status code 401 and do not process the request.
- Apply UserAuthenticator to your endpoints:
  - allow unauthenticated access to registration and authorization endpoints;
  - require authorization for all other endpoints.

### Task 3. Adding Game Logic for Two Players

- Add states for the current game:
  - Waiting for players;
  - Player’s turn with UUID;
  - Draw;
  - Victory for player with UUID.
- Add information about the marks (symbols) that users will use during the game.
- Improve the game-ending logic using the defined states.
- Add an endpoint for creating a new game with either a user or the computer.
- Add an endpoint to retrieve available current games.
- Add an endpoint for a user to join a game.
- Improve the endpoint for updating the current game, considering whether the opponent is a user or the computer.
- Add an endpoint to retrieve the current game.
- Add an endpoint to retrieve user information by UUID.