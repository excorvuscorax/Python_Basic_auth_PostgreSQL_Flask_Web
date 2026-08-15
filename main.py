from flask import Flask

from datasource.database import db
from di.container import Container
from web.route.game_route import register_game_route
from web.route.auth_route import register_auth_route

from web.route.page_route import page_blueprint
from web.route.user_route import register_user_route

app = Flask(__name__, template_folder="web/templates")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://postgres:schoolpsswd@localhost:5433/tic_tac_toe"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)


with app.app_context():
    db.create_all()


container = Container()

app.register_blueprint(
    register_game_route(
        container.game_service,
        container.authenticator,
    )
)

app.register_blueprint(register_auth_route(container.auth_service))
app.register_blueprint(page_blueprint)
app.register_blueprint(register_user_route(container.user_service))

if __name__ == "__main__":
    app.run(debug=True)
