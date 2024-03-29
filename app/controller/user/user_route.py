from flask import Blueprint, jsonify, request
from app.models.user import User
from app.utils.database import db
from app.utils.api_response import api_response
from app.service.user_service import User_service
from app.controller.user.schema import update_user_request

# from app import bcrypt

user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/", methods=["GET"])
def getUser():
    user_service = User_service()
    users = user_service.get_users()
    return api_response(users, 200, "success")


@user_blueprint.route("/", methods=["POST"])
def postUser():
    try:
        user = User()
        data = request.json
        # hashed_password = bcrypt.generate_password_hash(data["password"]).decode(
        #     "utf-8"
        # )
        user.username = data["username"]
        user.email = data["email"]
        user.name = data["name"]
        user.password = data["password"]
        db.session.add(user)
        db.session.commit()
        return api_response(user.as_dict(), 201, "success")
    except Exception as e:
        return str(e), 500


@user_blueprint.route("/<int:user_id>", methods=["PUT"])
def updateUser(user_id):
    try:
        user_service = User_service()

        data = request.json

        updatedUser = user_service.update_user(user_id, data)
        return api_response(updatedUser, 200, "success")
    except Exception as e:
        return {"message": str(e), "code": 500}


@user_blueprint.route("/<int:user_id>", methods=["DELETE"])
def deleteUser(user_id):
    try:
        user_service = User_service()
        user_service.delete_user(user_id)
        return api_response({}, 204, "success")
    except Exception as e:
        return {"message": str(e), "code": 500}
