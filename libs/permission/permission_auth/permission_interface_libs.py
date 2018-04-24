#coding=utf-8
from models.permission.permission_model import Menu, Handler


obj_model = {
    "handler": Handler,
    "menu": Menu,

}
class PermissionAuth(object):
    def __init__(self):
        self.user_permission = set() #当前用户的所有权限
        self.obj_permission = ''

    def permission_auth(self, user,  name, types, model):
        #获取当前用户的权限
        print '=====permission_auth====='
        roles = user.roles
        for role in roles:
            for permission in role.permissions:
                self.user_permission.add(permission.strcode)

        #获取handler、menu的权限
        # obj_model['handler'] == Handler.by_name('')
        # obj_model['menu']  == Menu .by_name('')

        handler = model[types].by_name(name)
        if handler is None:
            return False
        permission = handler.permission
        print permission
        print '-1'*10
        self.obj_permission = permission.strcode

        #如果handler对应的权限存在用户的所有权限集合中，返回True
        print '-'*50
        print self.user_permission
        print self.obj_permission
        print '-' * 50
        if self.obj_permission in self.user_permission: # if  'files_manage_menu' in {'files_manage_menu'}
            return True
        return False

def menu_permission(self, menuname, types):
    if PermissionAuth().permission_auth(self.current_user, menuname, types, obj_model):
        return True
    return False


def handler_permission(handlername, types):
    def func(method):
        def wrapper(self, *args, **kwargs):             # 'showpermission', 'handler'
            if PermissionAuth().permission_auth(self.current_user, handlername, types, obj_model):
                return method(self, *args, **kwargs)
            else:
                self.write('您没有权限')
        return wrapper
    return func






