from app.models.user import User
from app.utils.database import db


class User_repo:
    def get_list_users(self):
        users = User.query.all()
        return users

    def update_user(self, user_id, data):
        user_obj = User.query.get(user_id)
        if not user_obj:
            raise FileNotFoundError("User not found")

        user_obj.name = data["name"]

        db.session.commit()
        return user_obj

    def delete_user(self, user_id):
        user_obj = User.query.get(user_id)
        if not user_obj:
            raise FileNotFoundError("User not found")
        db.session.delete(user_obj)
        db.session.commit()
        return
