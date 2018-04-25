#coding=utf-8
from libs.permission.permission_auth.permission_interface_libs import menu_permission
from libs.flash.flash_lib import get_flashed_messages
from libs.files.files_libs import msg_count


settings = dict(
    template_path='templates',
    static_path='static',
    cookie_secret='hah',
    login_url='/auth/user_login',
    xsrg_cookies=True,
    debug=True,
    ui_methods={
        "menu_permission": menu_permission,
        'get_flashed_messages':get_flashed_messages,
        'msg_count':msg_count,
                },
    pycket={
        'engine': 'redis',
        'storage': {
            'host': 'localhost',
            'port': '6379',
            'db_sessions': 5,
            'db_notifications': 11,
            'max_connections': 2 ** 31,
        },
        'cookies': {
            'expires_days': 30,
            'max_age': 5000000,
        }
    }
)