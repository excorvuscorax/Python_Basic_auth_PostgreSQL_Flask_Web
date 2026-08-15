from flask import Blueprint, render_template

page_blueprint = Blueprint(
    "page",
    __name__,
)


@page_blueprint.route("/")
def index():

    return render_template("auth.html")
