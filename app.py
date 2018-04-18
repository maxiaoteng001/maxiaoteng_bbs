import uuid

from flask import (
    Flask,
    render_template,
    request,
    flash,
    redirect,
    url_for,
    Blueprint,
)

# 引入配置文件secret_key
import config


# 创建一个Flask实例
from models.board import Board
from models.topic import Topic
from routes import current_user

app = Flask(__name__)

# 导入flask-bootstrap
# 创建bootstrap实例
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

app.secret_key = config.SECRET_KEY

# 注册蓝图
# 有一个url_prefix 可以用来给每个蓝图中的每个路由加一个前缀
# 访问todo_routes中的路由,自动增加前缀/to do
from routes.user import main as user_routes
app.register_blueprint(user_routes, )
from routes.topic import main as topic_routes, csrf_tokens

app.register_blueprint(topic_routes, url_prefix="/topic")
from routes.reply import main as reply_routes
app.register_blueprint(reply_routes, url_prefix="/reply")
from routes.board import main as board_routes
app.register_blueprint(board_routes)


@app.route("/<int:board_id>")
def index(board_id):
    user = current_user()
    if board_id == 0:
        #ms = Topic.cache_all()
        ts = Topic.find_all(deleted=False)
    else:
        #ms = Topic.cache_find(board_id)
        ts = Topic.find_all(board_id=board_id, deleted=False)
    token = str(uuid.uuid4())
    u = current_user()
    csrf_tokens['token'] = u.id
    boards = Board.find_all(deleted=False)
    return render_template("index.html", user=user, ts=ts, token=token, boards=boards)


@app.route("/")
def index1():
    return redirect(url_for('index', board_id=0))

@app.route("/about")
def about():
    user = current_user()
    return render_template('about.html', user=user)


if __name__ == '__main__':
    # templates自动重载
    app.jinja_env.auto_reload = True
    app.config.from_object('config')
    # 生成配置并且运行程序
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=2000,
    )
    # 项目入口
    app.run(**config)
