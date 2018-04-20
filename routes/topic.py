from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    abort,
)

from routes import *

from models.topic import Topic
from models.board import Board
from models.reply import Reply
from utils import log

main = Blueprint('topic', __name__)


import uuid
csrf_tokens = dict()
@main.route("/")
def index():
    return redirect(url_for('index', board_id=0))


@main.route('/<int:id>')
def detail(id):
    t = Topic.get(id)
    return render_template("topic/detail.html", user=current_user(), topic=t)


@main.route("/add", methods=["POST"])
def add():
    form = request.form
    u = current_user()
    m = Topic.new(form, user_id=u.id)
    # for i in range(1000):
    #     m = Topic.new(form, user_id=u.id)
    return redirect(url_for('.detail', id=m.id))


@main.route("/delete")
def delete():
    id = int(request.args.get('id'))
    token = request.args.get('token')
    u = current_user()
    # 判断 token 是否是我们给的
    if token in csrf_tokens and csrf_tokens[token] == u.id:
        csrf_tokens.pop(token)
        if u is not None:
            print('删除 topic 用户是', u, id)
            Topic.delete(id)
            return redirect(url_for('topic.index'))
        else:
            abort(404)
    else:
        abort(403)


@main.route("/new")
def new():
    user=current_user()
    bs = Board.find_all(deleted=False)
    return render_template("topic/new1.html", bs=bs, user=user)
