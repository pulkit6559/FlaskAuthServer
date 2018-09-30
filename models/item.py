import db

class ItemModel(db.Model):

    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision = 2))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()#.filter_by(id=1)
     
    @classmethod
    def save_to_db(cls, item):
        db.session.add(self)

        db.session.commit()

    @classmethod
    def delete_from_db(cls, item):
        db.session.delete(self)