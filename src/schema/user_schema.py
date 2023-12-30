from src.schema import Schema

class UserSchema(Schema().ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'registered_at')