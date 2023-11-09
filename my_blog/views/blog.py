from flask import render_template, Blueprint, flash, g, redirect, request, url_for
from werkzeug.exceptions import abort
from my_blog.models.post import Post
from my_blog.models.user import User
from my_blog.models.coment import Comentario  # Importa el modelo de Comentario
from my_blog import db
from my_blog.views.auth import login_required

blog = Blueprint('blog', __name__)

# Obtener un usuario
def get_user(id):
    user = User.query.get_or_404(id)
    return user

@blog.route("/")
def index():
    posts = Post.query.all()
    db.session.commit()
    return render_template('blog/index.html', posts=posts, get_user=get_user)

# Crear post
@blog.route('/blog/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
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

    return render_template('blog/create.html')

# Obtener un post
def get_post(id, check_author=True):
    post = Post.query.get(id)
    if post is None:
        abort(404, f'Id {id} de la publicación no existe.')
    if check_author and post.author != g.user.id:
        abort(404)
    return post



# Actualizar post
@blog.route('/blog/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
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

    return render_template('blog/update.html', post=post)

# Eliminar un post
@blog.route('/blog/delete/<int:id>')
@login_required
def delete(id):
    post = get_post(id)
    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('blog.index'))

#Comentar
@blog.route('/blog/comment/<int:id>', methods=['POST'])
@login_required
def comment(id):
    post = get_post(id, check_author=False)

    if request.method == 'POST':
        texto = request.form.get('comment_text')

        error = None
        if not texto:
            error = 'El comentario no puede estar vacío.'
        if error is not None:
            flash(error)
        else:
            comentario = Comentario(texto=texto, autor=g.user, post=post)
            db.session.add(comentario)
            db.session.commit()
            return redirect(url_for('blog.index', id=post.id))
        flash(error)

    return redirect(url_for('blog.index'))

