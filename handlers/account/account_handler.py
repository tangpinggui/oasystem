# coding=utf-8
from handlers.base.base_handler import BaseHandler
from libs.account import account_libs

class UserProfileHandler(BaseHandler):

    def get(self):
        self.render('account/account_profile.html', message=None)


class ProfileEditHandler(BaseHandler):

    def get(self):
        self.render('account/account_edit.html')

    def post(self):
        name = self.get_argument('name', '')
        password = self.get_argument('password', '')

        result = account_libs.user_edit(self, name, password)
        if result['status'] is False:
            self.render('account/account_profile.html', message=result['msg'])
        return self.render('account/account_profile.html', message=result['msg'])


class ProfileModifyEmailHandler(BaseHandler):

    def get(self):
        self.render('account/account_send_email.html')

    def post(self):
        email = self.get_argument('email', '')

        result = account_libs.send_email_libs(self, email)
        if result['status'] is False:
            return self.write(result['msg'])
        return self.write(result['msg'])


class ProfileAuthEmailHandler(BaseHandler):

    def get(self):
        email_code = self.get_argument('code', '')
        email = self.get_argument('email', '')
        u = self.get_argument('user_id', '')

        result = account_libs.auth_email_libs(self, email_code, email, u)

        if result['status'] is True:
            return self.redirect('/account/user_edit')
        return self.write(result['msg'])


class AvatarAddHandler(BaseHandler):

    def post(self):
        avatar_data = self.request.files.get('user_avatar', '')
        if avatar_data:
            result = account_libs.add_avatar_libs(self, avatar_data[0]['body'])
            if result['status'] is True:
                return self.redirect("/account/user_edit")
            return self.write(result['msg'])
        return self.write('please choice a picture')