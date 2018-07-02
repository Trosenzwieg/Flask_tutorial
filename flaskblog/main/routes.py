from flask import render_template, request, Blueprint
from flask_login import login_required
from flaskblog.models import Post

main = Blueprint('main',__name__)

@main.route("/")
@main.route("/home")
@login_required
def home():
    page = request.args.get('page', 1, type=int)
    post = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)
    return render_template('home.html', posts=post)


@main.route("/about")
@login_required
def about():
    return render_template('about.html',title='About')