from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from resources.user import UserRegister
from resources.item import Item, ItemList
from security import authenticate, identity

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # To allow flask propagating exception even if debug is set to false on app
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)

#no longer in memory database

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)  #to prevent circular import
    app.run(debug=True)  # important to mention debug=True

