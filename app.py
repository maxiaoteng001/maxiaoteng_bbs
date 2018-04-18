
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
from routes.topic import main as topic_routes
app.register_blueprint(topic_routes, url_prefix="/topic")


@app.route("/")
def index():
    return render_template('index.html', user=None)


@app.route("/about")
def about():
    return render_template('about.html', user=None)


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
