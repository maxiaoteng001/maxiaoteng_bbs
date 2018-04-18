import hashlib

from models.mongua import Mongua


class User(Mongua):
    __fields__ = Mongua.__fields__ + [
        ('username', str, ''),
        ('password', str, ''),
        ('email', str, ''),
        ('admin', bool, False),
        ('user_image', str, '')
    ]

    def __init__(self):
        self.user_image = 'default.png'

    def salted_password(self, password, salt="maxiaoteng"):

        def sha256(ascii_str):
            return hashlib.sha256(ascii_str.encode('ascii')).hexdigest()

        hash1 = sha256(password)
        hash2 = sha256(hash1 + salt)
        return hash2

    # 基本的hash加密, 获取摘要字符串
    def hashed_password(self, pwd):
        p = pwd.encode('ascii')
        s = hashlib.sha256(p)
        return s.hexdigest()

    @classmethod
    def register(cls, form):
        name = form.get('username', '')
        pwd = form.get('password', '')
        pwd1 = form.get('password1', '')

        if pwd == pwd1 and len(pwd) > 2 and User.find_by(username=name) is None:
            u = User.new(form)
            u.password = u.salted_password(pwd)
            u.save()
            return u
        else:
            return None

    @classmethod
    def validate_login(cls, form):
        u = User()
        u.username = form.get('username', '')
        u.password = form.get('password', '')
        user = User.find_by(username=u.username)
        if user is not None and user.password == u.salted_password(password=u.password):
            return user
        else:
            return None
