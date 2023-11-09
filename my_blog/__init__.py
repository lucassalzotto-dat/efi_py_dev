from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.app_context().push()


app.config.from_object('config.DevelopmentConfig')

db =  SQLAlchemy(app)

#Importar vistas
from my_blog.views.auth import auth

app.register_blueprint(auth)

from my_blog.views.blog import blog
app.register_blueprint(blog)


db.create_all()

