#coding=utf-8
from random import randint
from utils.captcha.captcha import create_captcha
from models.account.account_user_model import User
from datetime import datetime

from libs.yun_tong_xun.yun_tong_xun_lib import sendTemplateSMS


def create_captcha_img(self, pre_code, code):
    '''
    返回一个验证码图片
        :pre_code js设置的两个属性用来重置验证码
        :code
     '''
    if pre_code:
        self.conn.delete("captcha:%s" % pre_code)
    text, img = create_captcha()
    self.conn.setex("captcha:%s" % code, text.lower(), 60 )
    return img

def auth_captcha(self, captcha_code, code):
    ''' 判断用户输入的验证码是否正确 '''
    if captcha_code == '':
        return {'status':False, 'msg': '请输入图形验证码'}

    elif self.conn.get('captcha:%s' %code) != captcha_code.lower():
        return {'status': False, 'msg': '输入的图形验证码不正确'}

    return {"status":True, 'msg':'正确'}

def login(self, name, password):
    ''' user login '''
    if name == '' and password == '':
        return {'status': False, 'msg': '用户名和密码不能为空'}
    user = User.by_name(name)
    if user and user.auth_password(password):
        user.last_login = datetime.now()
        user.loginnum += 1
        self.db.add(user)
        self.db.commit()
        self.session.set('username', name)
        return {"status":True, 'msg':'登陆成功'}
    return {'status': False, 'msg': '用户名或密码不正确'}

def regist(self, name, mobile,mobile_captcha, password1, password2, agree):
    ''' user rigist '''
    if agree == '':
        return {'status': False, 'msg': "您没有点击同意条款"}

    if password1 != password2:
        return {'status': False, 'msg': "两次输入密码不一致"}

    if self.conn.get('mobile_code:%s' % mobile) != mobile_captcha:
        return {'status': False, 'msg': "短信验证码错误"}

    user = User.by_name(name)
    if user:
        return {'status': False, 'msg': "用户名已经存在"}

    user = User()
    user.name = name
    user.password = password1
    user.mobile = mobile
    self.db.add(user)
    self.db.commit()
    print 'True'
    return {'status': True, 'msg': '注册成功'}

def get_mobile_code(self, mobile):
    ''' 发送手机验证码 '''
    if isinstance(mobile, unicode):
        mobile = mobile.decode('utf-8')

    mobile_code = randint(1000,9999)
    print '手机验证码是%s' % mobile_code
    # sendTemplateSMS(mobile, [mobile_code, 30], 1)
    self.conn.setex('mobile_code:%s' % mobile, mobile_code, 2000)
    return {"status": True, 'msg': '验证码已发送，注意查收'}