# models.py

from flask_login import UserMixin

class User(UserMixin):
    pass

users = [
]

def addusers(user):
    users.append(user)

def query_user(user_id):
    for user in users:
        if user_id == user['id']:
            return user