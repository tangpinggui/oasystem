# coding=utf-8
from handlers.base.base_handler import BaseHandler
from libs.permission import permission_list_libs
from libs.flash.flash_lib import get_flashed_messages
from libs.permission.permission_auth.permission_interface_libs import handler_permission


class PermissionManageHandler(BaseHandler):
    ''' 权限管理 '''
    @handler_permission('showpermission','handler')
    def get(self):
        roles, permissions, menus, handlers, users = permission_list_libs.permission_manager_list_lib(self)
        kw = {
            'roles': roles,
            'permissions': permissions,
            'menus': menus,
            'handlers': handlers,
            'users': users,
        }
        return self.render('permission/permission_list.html', **kw)


class UserAddRoleHandler(BaseHandler):
    ''' 为用户添加角色 '''

    def post(self):
        user_id = self.get_argument('userid', '')
        role_id = self.get_argument('roleid', '')
        result = permission_list_libs.user_add_role(self, user_id, role_id)

        if result['status'] is True:
            return self.redirect('/permission/manage')
        self.write(result['msg'])


class RoleAddPermissionHandler(BaseHandler):
    ''' 为角色添加权限 '''
    def post(self):
        permission_id = self.get_argument('permissionid', '')
        role_id = self.get_argument('roleid', '')
        result = permission_list_libs.role_add_permission(self, permission_id, role_id)

        if result['status'] is True:
            return self.redirect('/permission/manage')
        self.write(result['msg'])


class AddRoleHandler(BaseHandler):
    ''' 添加角色 '''

    def post(self):
        role_name = self.get_argument('name', '')
        result = permission_list_libs.save_role_name(self, role_name)
        self.redirect('/permission/manage')

class DelRoleHandler(BaseHandler):
    ''' 删除角色 '''

    def get(self):
        role_id = self.get_argument('id', '')
        result = permission_list_libs.del_role_name(self, role_id)
        if result['status'] is False:
            return self.write(result['msg'])
        self.redirect('/permission/manage')


class AddPermissionCodeHandler(BaseHandler):
    ''' 添加权限名和权限码 '''

    def post(self):
        permission_name = self.get_argument('name', '')
        permission_code = self.get_argument('strcode', '')
        print permission_name, permission_code
        print type(permission_name), permission_code
        result = permission_list_libs.permission_add_code(self, permission_name, permission_code)
        if result['status'] is True:
            return self.redirect('/permission/manage')
        self.write(result['msg'])



class DelPermissionCodeHandler(BaseHandler):
    ''' 删除权限码和权限名 '''

    def get(self):
        permission_id = self.get_argument('id', '')
        print '--'*10, id
        result = permission_list_libs.permission_del_code(self, permission_id)
        if result['status'] is True:
            return self.redirect('/permission/manage')
        self.write(result['msg'])

import time
class MenuAddPermissionHandler(BaseHandler):
    ''' 为菜单添加权限 '''

    def post(self):
        name = self.get_argument('name', '')
        permissionid = self.get_argument('permissionid', '')
        result = permission_list_libs.menu_add_p_lib(self, name, permissionid)
        if result['status'] is True:
            return self.redirect('/permission/manage')
        self.write(result['msg'])


class MenuDelPermissionHandler(BaseHandler):
    ''' 删除菜单权限 '''
    def get(self):
        menuid = self.get_argument('menuid', '')
        result = permission_list_libs.del_menu_permission(self, menuid)
        if result['status'] is True:
            return self.redirect('/permission/manage')
        self.write(result['msg'])


class AddHandler(BaseHandler):
    ''' 为处理器添加权限 '''
    def post(self):
        view_name = self.get_argument('name', '')
        permission_id = self.get_argument('permissionid', '')
        result = permission_list_libs.add_handler(self, view_name, permission_id)
        if result['status'] is True:
            return self.redirect('/permission/manage')
        self.write(result['msg'])


class DelHandler(BaseHandler):
    ''' 删除处理器权限 '''
    def get(self):
        handlerid = self.get_argument('handlerid', '')
        result = permission_list_libs.del_handler(self, handlerid)
        if result['status'] is True:
            return self.redirect('/permission/manage')
        self.write(result['msg'])


class DelUserHandler(BaseHandler):
    ''' 删除用户 '''
    def get(self):
        user_id = self.get_argument('userid', '')
        result = permission_list_libs.del_user(self, user_id)
        if result['status'] is True:
            return self.redirect('/permission/manage')
        self.write(result['msg'])
