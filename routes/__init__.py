# 定义一个函数,将字典类型的列表序列化 转化成字符串
import json

from flask import session

from models.user import User


def json_response(data):
    """
    本函数返回 json 格式的 body 数据
    前端的 ajax 函数就可以用 JSON.parse 解析出格式化的数据
    """
    # json.dumps 用于把 list 或者 dict 转化为 json 格式的字符串
    # ensure_ascii=False 可以正确处理中文
    # indent=2 表示格式化缩进, 方便好看用的
    body = json.dumps(data, ensure_ascii=False, indent=2)
    # log('序列化后的body', body)
    return body


def current_user():
    # 从session中找到user_id的字段,找不到返回-1
    # 然后通过find_by来用id找到用户
    # 找不到返回None
    username = session.get('username', -1)
    u = User.find_by(username=username)
    return u
