from my_blog import db
from my_blog.schemas.UserSchema import UserSchema

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.Text)

    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

    def to_dict(self):
        schema = UserSchema()
        return schema.dump(self)
