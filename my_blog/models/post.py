from datetime import datetime
from my_blog import db

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
    dateTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self,author,title, body) -> None:
        self.author = author
        self.title = title
        self.body = body
        
    def __repr__(self) -> str:
        return f'Post:{self.title}'        