# coding=utf-8
from handlers.message import message_handler


message_urls = [
    (r"/message/message", message_handler.MessageHandler),
    (r"/message/message_websocket", message_handler.WebSocketHandler),
    (r"/message/send_message", message_handler.SendMessageHandler),
]