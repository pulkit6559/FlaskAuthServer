from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel
import sqlite3 



class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with the name {} already exists".format(name)}, 400
        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}

        try:
            ItemModel.save_to_db(item)
        except:
            return {"message": 'An error occoured while inserting'}
        return item, 500 #internal server error

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete()

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        # Once again, print something not in the args to verify everything works
        item = ItemModel.find_by_name(name)
        updated_item = {'name': name, 'price': data['price']}
        
        if item is None:
            item = ItemModel(name, data['price'])
            else:
            try:
                item.price = data['price']
            except:
                return {"message": "error occoured while updating"}, 500
        item.save_to_db()
        return item.json()



class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)

        items = []
        
        for row in result:
            items.append({'name': row[0], 'price': row[1]})


        connection.commit()
        connection.close()
