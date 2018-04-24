# coding=utf-8
import json
import traceback
from datetime import datetime
from models.account.account_user_model import User
from string import printable
from random import choice
from uuid import uuid4
from libs.common.send_email.send_email_libs import send_qq_html_email


def user_edit(self, name, password):
    if name == '' or password == '':
        return {'status': False, 'msg': '用户密码不能为空'}
    user = User.by_name(name)
    user.password = password
    user.name = name
    user.update_time = datetime.now()
    self.db.add(user)
    self.db.commit()
    self.session.set('username',name)
    return {'status': True, 'msg': '修改成功啦'}


def send_email_libs(self, email):
    ''' 生成验证码，发送链接注册邮件到用户，返回的url用get方式返回数据 '''
    if email == '':
        return {'status': False, 'msg': '请输入邮箱'}
    email_code = ''.join([choice(printable[:62]) for i in xrange(4)])
    print email_code
    u = str(uuid4())

    text_dict = {
        u: self.current_user.id,
        'email_code': email_code
    }
    redis_dict= json.dumps(text_dict)

    self.conn.setex('email%s' % email, redis_dict, 500)

    content = """
        <p>html注册邮件</p>
        <a href = "http://127.0.0.1:8000/account/auth_email_code?code={}&email={}&user_id={}">点击绑定邮箱</a>
    """.format(email_code, email, u)
    send_qq_html_email('624764516@qq.com', [email],'第一课', content)
    return {'status': True, 'msg': '邮箱发送成功'}


def auth_email_libs(self, email_code, email, u):
    redis_text = self.conn.get('email%s' % email)
    if redis_text:
        text_dict = json.loads(redis_text)
        if redis_text and email_code == text_dict['email_code']:
            user = self.current_user
            if not user:
                user = user.by_id(text_dict[u])

            user.email = email
            user.update_time = datetime.now()
            self.db.add(user)
            self.db.commit()
            return {'status': True, 'msg': '邮箱修改成功'}
        return {'status': False, 'msg': '邮箱验证码不正确'}
    return {'status': False, 'msg': '邮箱验证码已过期，请重新绑定'}


def add_avatar_libs(self, avatar_data):
    try:
        user = self.current_user
        user.avatar = avatar_data
        user.update_time = datetime.now()
        print user
        self.db.add(user)
        self.db.commit()
        print 'ha'
        return {'status': True}
    except Exception as e:
        print '-' * 10
        print traceback.format_exc()
        print '-' * 10
        return {'status': False, 'msg': 'error'}