from app.models.user import User
from app.utils.database import db


class User_repo:
    def get_list_users(self):
        users = User.query.all()
        return users

    def update_user(self, user_id, user):
        user = User.query.get(user_id)
        if not user:
            return {"message": "User does not exist"}, 404
        user.name = user.name
        db.session.add(user)
        db.session.commit()
        return {"message": "Success update user"}, 201
