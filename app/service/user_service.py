from app.repositories.user_repo import User_repo


class User_service:
    def __init__(self):
        self.user_repo = User_repo()

    def get_users(self):
        users = self.user_repo.get_list_users()
        return [user.as_dict() for user in users]

    def update_user(self, user_id, data):
        updated_user = self.user_repo.update_user(user_id, data)
        return updated_user.as_dict()

    def delete_user(self, user_id):
        self.user_repo.delete_user(user_id)
        return
