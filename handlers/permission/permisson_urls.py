# coding=utf-8
from handlers.permission import permisson_handler


permission_urls = [
    (r'/permission/user_add_role', permisson_handler.UserAddRoleHandler),
    (r'/permission/role_add_permission', permisson_handler.RoleAddPermissionHandler),
    (r'/permission/manage', permisson_handler.PermissionManageHandler),
    (r'/permission/add_role', permisson_handler.AddRoleHandler),
    (r'/permission/del_role', permisson_handler.DelRoleHandler),
    (r'/permission/add_permission', permisson_handler.AddPermissionCodeHandler),
    (r'/permission/del_permission', permisson_handler.DelPermissionCodeHandler),
    (r'/permission/add_menu', permisson_handler.MenuAddPermissionHandler),
    (r'/permission/del_menu', permisson_handler.MenuDelPermissionHandler),
    (r'/permission/add_handler', permisson_handler.AddHandler),
    (r'/permission/del_handler', permisson_handler.DelHandler),
    (r'/permission/del_user_role', permisson_handler.DelUserHandler),
]