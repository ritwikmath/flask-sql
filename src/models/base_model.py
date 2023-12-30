from src.schema.user_schema import UserSchema

class BaseModel:
    def serialize(self, data):
        if isinstance(data, list):
            schema = UserSchema(many=True)
        else:
            schema = UserSchema()
        return schema.dump(data)
