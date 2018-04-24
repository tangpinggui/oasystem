#coding=utf-8
from main_handler import MainHandler
from handlers.account.account_urls import account_urls
from handlers.permission.permisson_urls import permission_urls
from handlers.article.article_urls import article_urls
from handlers.files.files_urls import files_urls
from tornado.web import StaticFileHandler
from handlers.message.message_urls import message_urls


handlers = [
    (r'/', MainHandler),
    (r'/images/(.*\.(jpg|mp3|mp4|ogg|png))', StaticFileHandler, {'path': 'files/'}), # 声明路劲
]

handlers += account_urls
handlers += permission_urls
handlers += article_urls
handlers += files_urls
handlers += message_urls
