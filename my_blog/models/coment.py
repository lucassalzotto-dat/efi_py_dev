from my_blog.models.user import User
from my_blog.models.post import Post
from datetime import datetime
from my_blog import db

class Comentario(db.Model):
    __tablename__ = 'comentarios'
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.Text, nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relación con el modelo User (uno a muchos: un usuario puede tener varios comentarios)
    autor_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    autor = db.relationship('User', backref='comentarios')
    
    # Relación con el modelo Post (uno a muchos: un post puede tener varios comentarios)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    post = db.relationship('Post', backref='comentarios')

    def __init__(self, texto, autor, post):
        self.texto = texto
        self.autor = autor
        self.post = post
