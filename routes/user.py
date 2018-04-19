from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    session)

from models.user import User
# 创建一个蓝图对象
# 然后在falsk主代码中[注册蓝图]来使用
# 第一个是蓝图的名字, 在app.py的时候使用
# 第二个是套路
from utils import log

main = Blueprint('user', __name__)


# 登录页面
@main.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        # user = current_user()
        return render_template('user/signin.html', user=None)
    elif request.method == 'POST':
        form = request.form
        user = User.validate_login(form)
        if user is None:
            # 登录失败
            log('登录失败')
            return redirect(url_for('.signin'))
        else:
            # 登录成功
            log('登录成功', user.username)
            session['username'] = user.username
            session.permanent = True
            return redirect(url_for('topic.index'))


@main.route('/signout')
def signout():
    session.pop('username', None)
    return redirect(url_for('index'))


@main.route('/signup', methods=['get', 'post'])
def signup():
    if request.method == 'GET':
        return render_template('user/signup.html', user=None)
    elif request.method == 'POST':
        form = request.form
        user = User.register(form)
        if user is None:
            return '注册失败 <a href="/signup">请重新注册</a>'
        return render_template('user/signupSuccess.html', username=user.username)


@main.route('/search_pass', methods=['get', 'post'])
def search_pass():
    if request.method == 'GET':
        return '找回密码功能暂未开通'
        # return render_template('user/search_pass.html', user=None)
    # elif request.method == 'POST':
        # form = request.form
        # user = User.register(form)
        # if user is None:
        #     return '找回密码失败 <a href="url_for(".search_pass")">请重新找回</a>'
        # return render_template('user/signupSuccess.html', username=user.username)


@main.route('/user/<username>')
def user_detail(username):
    user = User.find_by(username=username)
    return render_template('user/user_detail.html', user=user)


@main.route('/user/edit/<username>')
def user_edit(username):
    user = User.find_by(username=username)
    return render_template('user/user_edit.html', user=user)

