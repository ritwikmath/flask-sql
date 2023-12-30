from flask_marshmallow import Marshmallow

class Schema:
    instance = None
    schema = None
    def __new__(cls):
        if cls.instance == None:
            cls.instance = super(Schema, cls).__new__(cls)
        return cls.instance
    
    @property
    def ma(self):
        if not self.schema:
            raise Exception("Schema is not set yet")
        return self.schema
    
    @ma.setter
    def ma(self, app):
        self.schema = Marshmallow(app)