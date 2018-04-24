#coding=utf-8
import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.escape
from tornado.options import define, options
from config import settings
from handlers.main.main_urls import handlers
# from models.account.account_user_model import User
# from models.files.upload_file_model import Files
# from models.article import article_model
from libs.db import create_talbes
from libs.db.dbsession import dbSession
from models.account.account_user_model import User
from models.files.upload_file_model import Files


from models.permission.permission_model import (
    Role, Permission, PermissionToRole, UserToRole, Handler, Menu
)
from models.article.article_model import (
    Article, ArticleToTag, UserLikeArticle, Category,Comment,SecondComment, Tag)


#定义一个默认的端口
define("port", default=8000, help="run port ", type=int)
define("runserver", default=False, help="start server", type=bool)
define("t", default=False, help="create table", type=bool)
define("u", default=False, help="create user", type=bool)



if __name__ == "__main__":
    options.parse_command_line()
    if options.t:
        create_talbes.run()

    if options.u:
        user = User()
        user.name = 'zhangsan'
        user.password = '222'
        dbSession.add(user)
        dbSession.commit()

    if options.runserver:
        app = tornado.web.Application(handlers, **settings) #创建应用实例
        http_server = tornado.httpserver.HTTPServer(app) #通过应用实例创建服务器实例
        http_server.listen(options.port)  #监听8000端口 listen单线程 bind可实现多线程
        print 'start server...'
        tornado.ioloop.IOLoop.instance().start() #启动服务器

