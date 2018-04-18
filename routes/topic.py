from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
)

from models.todo import Todo
from routes import current_user, json_response
from utils import log

# 创建一个蓝图对象
# 然后在flask主代码中[注册蓝图]来使用
# 第一个是蓝图的名字, 在app.py的时候使用
# 第二个是套路
main = Blueprint('topic', __name__)


@main.route('/xx', methods=['GET'])
# 显示todo首页,也就是查找所有todo并返回
def index():
    user = current_user()
    log('当前登录用户:', user)
    # 如果用户未登陆, 跳转到首页, 表示未登录状态
    if user is None:
        return redirect(url_for("user.signin"))
    else:
        todos = Todo.find_all(user_id=user.id, deleted=False)
        return render_template("/todo/todo_index.html", user=user, todos=todos)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    t = Todo.new(form)
    t.save()
    return redirect(url_for('todo.index'))


@main.route('/complete/<int:id>')
def complete_todo(id):
    t = Todo.complete(id)
    if t is not None:
        return json_response(t.json())
    else:
        return redirect(url_for('todo.index'))


@main.route('/delete/<int:id>')
def delete_todo(id):
    t = Todo.find(id)
    t = t.delete()
    if t is not None:
        return json_response(t.json())
    else:
        return redirect(url_for('todo.index'))
