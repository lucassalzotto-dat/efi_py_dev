from flask import render_template, Blueprint, flash, g, redirect, request, url_for
from flask.views import MethodView
from werkzeug.exceptions import abort
from my_blog.models.post import Post
from my_blog.models.user import User
from my_blog.models.coment import Comentario
from my_blog import db
from my_blog.views.auth import login_required

blog = Blueprint('blog', __name__)

# Obtener un usuario
def get_user(id):
    user = User.query.get_or_404(id)
    return user

# Obtener un post
def get_post(id, check_author=True):
    post = Post.query.get(id)
    if post is None:
        abort(404, f'Id {id} de la publicación no existe.')
    if check_author and post.author != g.user.id:
        abort(404)
    return post

# Vistas de MethodView

class IndexView(MethodView):
    def get(self):
        posts = Post.query.all()
        return render_template('blog/index.html', posts=posts, get_user=get_user)

class CreateView(MethodView):
    decorators = [login_required]

    def get(self):
        return render_template('blog/create.html')

    def post(self):
        title = request.form.get('title')
        body = request.form.get('body')

        post = Post(g.user.id, title, body)

        error = None
        if not title:
            error = 'Se requiere un titulo'
        if error is not None:
            flash(error)
        else:
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('blog.index'))
        flash(error)

class UpdateView(MethodView):
    decorators = [login_required]

    def get(self, id):
        post = get_post(id)
        return render_template('blog/update.html', post=post)

    def post(self, id):
        post = get_post(id)
        post.title = request.form.get('title')
        post.body = request.form.get('body')

        error = None
        if not post.title:
            error = 'Se requiere un titulo'
        if error is not None:
            flash(error)
        else:
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('blog.index'))
        flash(error)

class DeleteView(MethodView):
    decorators = [login_required]

    def get(self, id):
        post = get_post(id)
        
        # Eliminar los comentarios asociados al post
        comentarios_asociados = Comentario.query.filter_by(post_id=post.id).all()
        for comentario in comentarios_asociados:
            db.session.delete(comentario)

        db.session.delete(post)
        db.session.commit()

        return redirect(url_for('blog.index'))

class CommentView(MethodView):
    decorators = [login_required]

    def post(self, id):
        post = get_post(id, check_author=False)

        texto = request.form.get('comment_text')

        error = None
        if not texto:
            error = 'El comentario no puede estar vacío.'
        elif post is None or post.id is None:
            error = 'Error al obtener el post o el post no tiene un ID válido.'
        else:
            comentario = Comentario(texto=texto, autor=g.user, post=post)
            db.session.add(comentario)
            db.session.commit()
            return redirect(url_for('blog.index'))
        
        flash(error)

        return redirect(url_for('blog.index'))

# Agregar las rutas con las clases MethodView
blog.add_url_rule('/', view_func=IndexView.as_view('index'))
blog.add_url_rule('/blog/create', view_func=CreateView.as_view('create'))
blog.add_url_rule('/blog/update/<int:id>', view_func=UpdateView.as_view('update'))
blog.add_url_rule('/blog/delete/<int:id>', view_func=DeleteView.as_view('delete'))
blog.add_url_rule('/blog/comment/<int:id>', view_func=CommentView.as_view('comment'))
