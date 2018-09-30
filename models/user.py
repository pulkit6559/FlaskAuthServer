import sqlite3

class UserModel(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))  #tuple
        row = result.fetchone()
        if row:
            user = cls(*row)  #User(row[0],row[1],row[2])
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))  #tuple
        row = result.fetchone()
        if row:
            user = cls(*row)  #User(row[0],row[1],row[2])
        else:
            user = None

        connection.close()
        return user