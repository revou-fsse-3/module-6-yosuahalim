import os
from flask import Flask, request
from markupsafe import escape
from app.controller.user import user_route
from app.utils.database import db, migrate
from app.models.user import User

# from flask_bcrypt import Bcrypt


DATABASE_TYPE = os.getenv("DATABASE_TYPE")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_PORT = os.getenv("DATABASE_PORT")


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"{DATABASE_TYPE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate.init_app(app, db)
# bcrypt = Bcrypt(app)

# app.register_blueprint(pokemon.pokemon_blueprint, url_prefix="/pokemon")
app.register_blueprint(user_route.user_blueprint, url_prefix="/user")


@app.route("/")
def hello_world():
    users = User.query.all()
    results = [{"name": user.username} for user in users]
    print(results)
    return {"data": results}


@app.route("/post-message", methods=["POST"])
def post_message():
    try:
        return {"message": "hellow world"}
    except Exception as e:
        print(e)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
