from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
)

from routes import *

from models.board import Board
from utils import log

main = Blueprint('board', __name__)


@main.route("/admin")
def index():
    user = current_user()
    if user.admin is False:
        return redirect(url_for('index'))
    bs = Board.find_all(deleted=False)
    if bs = []:
        bs = None
    return render_template('board/admin_index.html', user=user, boards=bs)



@main.route("/admin/add_board", methods=["POST"])
def add():
    form = request.form
    u = current_user()
    b = Board.new(form)
    return redirect(url_for('board.index'))

@main.route("/admin/delete_board/<int:id>")
def delete(id):
    u = current_user()
    # u.admin = True
    if u.admin is True:
        m = Board.find(id)
        m = m.delete()
        return json_response(m.json())
    else:
        return "没有权限"


