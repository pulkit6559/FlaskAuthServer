from werkzeug.security import safe_str_cmp
from resources.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload): #payload is contents of JWT tokens used to check is user is authenticated
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
