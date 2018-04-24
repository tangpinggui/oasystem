# coding=utf-8
from models.permission.permission_model import Role, Permission, Menu, Handler, UserToRole, PermissionToRole
from models.account.account_user_model import User
from libs.flash.flash_lib import flash


def permission_manager_list_lib(self):
    ''' 返回给权限管理页面 '''
    roles = Role.all()
    permissions = Permission.all()
    menus = Menu.all()
    handlers = Handler.all()
    users = User.all()
    return roles, permissions, menus, handlers, users


def save_role_name(self, role_name):
    ''' 存入新增角色名 '''
    if role_name == '':
        flash(self, "角色不能为空", "error")
        return
    role = Role.by_name(role_name)
    if role is not None:
        flash(self, "角色已经存在", "error")
        return

    role = Role()
    role.name = role_name
    self.db.add(role)
    self.db.commit()
    flash(self, "角色添加成功", "success")


def del_role_name(self, role_id):
    ''' 删除角色名 '''
    role = Role.by_id(role_id)
    if role:
        self.db.delete(role)
        self.db.commit()
        flash(self, "删除成功", "success")
        return {'status': True}
    return {'status': False, 'msg': '不存在的ID'}


def user_add_role(self, user_id, role_id):
    ''' 给用户添加角色 '''
    user = User.by_id(user_id)
    if user is None:
        return {'status': False, 'msg': '不存在该用户ID'}
    role = Role.by_id(role_id)
    if role is None:
        return {'status': False, 'msg': '不存在该角色ID'}
    user_role = UserToRole()
    user_role.r_id = role_id
    user_role.u_id = user_id
    self.db.add(user_role)
    self.db.commit()
    return {'status': True}


def role_add_permission(self, permission_id, role_id):
    ''' 给角色增加权限 '''
    role = Role.by_id(role_id)
    permission = Permission.by_id(permission_id)
    if permission is None:
        return {'status': False, 'msg': '不存在该权限ID'}
    if role is None:
        return {'status': False, 'msg': '不存在该角色ID'}
    '''
    第一种保存数据
    permission_role = PermissionToRole()
    permission_role.r_id = role_id
    permission_role.p_id = permission_id
        '''
    permission.roles.append(role) # 第二种
    self.db.add(permission)
    self.db.commit()
    return {'status': True}


def permission_add_code(self, permission_name, permission_code):
    ''' 添加权限名和权限码 '''
    if permission_name == '':
        return {'status': False, 'msg': '请输入权限名'}
    if permission_code == '':
        return {'status': False, 'msg': '请输入权限码'}
    permission = Permission()
    permission.name = permission_name
    permission.strcode = permission_code
    self.db.add(permission)
    self.db.commit()
    return {'status': True, 'msg': '添加成功'}


def permission_del_code(self, permission_id):
    ''' 删除权限名和权限码 '''
    permission = Permission.by_id(permission_id)
    if permission:
        self.db.delete(permission)
        self.db.commit()
        return {'status': True}
    return {'status': False, 'msg': '不存在的ID'}


def menu_add_p_lib(self, name, permissionid):
    ''' 为菜单添加权限 '''
    if name == '' or permissionid == '':
        return {'status': False, 'msg': '无效的权限ID'}
    permission = Permission.by_id(permissionid)
    if permission is None:
        return {'status': False, 'msg': '无效的权限ID'}
    menu = Menu.by_name(name)
    if menu:
        menu.p_id = permissionid
        self.db.add(menu)
        self.db.commit()
        return {'status': True}
    menu = Menu()
    menu.name = name
    menu.p_id = permissionid
    self.db.add(menu)
    self.db.commit()
    return {'status': True}


def del_menu_permission(self, menuid):
    ''' 删除菜单权限 '''
    menu = Menu.by_id(menuid)
    if menu is None:
        return {'status': False, 'msg': '不存在这条信息'}
    self.db.delete(menu)
    self.db.commit()
    return {'status': True}


def add_handler(self,view_name, permission_id):
    ''' 为处理器添加权限  '''

    if view_name == '' or permission_id == '':
        return {'status': False, 'msg': '请输入视图名和权限名'}
    permission = Permission.by_id(permission_id)
    if permission is None:
        return {'status': False, 'msg': '请输入有效的权限ID'}
    handler = Handler.by_name(view_name)
    if handler:
        handler.p_id = permission_id
        self.db.add(handler)
        self.db.commit()
        return {'status': True}
    handler = Handler()
    handler.name = view_name
    handler.p_id = permission_id
    self.db.add(handler)
    self.db.commit()
    return {'status': True}


def del_handler(self, handlerid):
    ''' 删除处理器权限 '''
    handler = Handler.by_id(handlerid)
    if handler is None:
        return {'status': False, 'msg': '该信息不存在'}
    self.db.delete(handler)
    self.db.commit()
    return {'status': True}


def del_user(self, user_id):
    ''' 删除用户 '''
    user = User.by_id(user_id)
    self.db.delete(user)
    self.db.commit()
    return {'status': True}
