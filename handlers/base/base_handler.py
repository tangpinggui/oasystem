#coding=utf-8
import tornado.escape
import tornado.web
import tornado.websocket

from libs.pycket.session import SessionMixin
from libs.db.dbsession import dbSession
from libs.redis_conn.redis_conn import conn
from models.account.account_user_model import User


class BaseHandler(tornado.web.RequestHandler, SessionMixin):
    def initialize(self):
        self.db=dbSession #操作mysql
        self.conn = conn #操作redis
        self.flashes = None # flush函数的参数通过self.调用


    def get_current_user(self):
        """获取当前用户"""
        username = self.session.get("username")
        user = None
        if username:
            user = User.by_name(username)
        return user if user else None


    def on_finish(self):
        self.db.close()


class WebBaseHandler(tornado.websocket.WebSocketHandler, SessionMixin):
    def initialize(self):
        self.db=dbSession #操作mysql
        self.conn = conn #操作redis
        self.flashes = None # flush函数的参数通过self.调用


    def get_current_user(self):
        """获取当前用户"""
        username = self.session.get("username")
        user = None
        if username:
            user = User.by_name(username)
        return user if user else None


    def on_finish(self):
        self.db.close()