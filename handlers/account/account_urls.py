#coding=utf-8
import account_handler
import account_auth_handler


account_urls = [
    (r'/auth/user_login', account_auth_handler.LoginHandler),
    (r'/auth/captcha', account_auth_handler.CaptchaHandler),
    (r'/auth/user_regist', account_auth_handler.RegistHandler),
    (r'/auth/mobile_code', account_auth_handler.MobileCaptchaHandler),
    (r'/account/user_profile', account_handler.UserProfileHandler),
    (r'/account/user_edit', account_handler.ProfileEditHandler),
    (r'/account/send_user_email', account_handler.ProfileModifyEmailHandler),
    (r'/account/auth_email_code', account_handler.ProfileAuthEmailHandler),
    (r'/account/avatar', account_handler.AvatarAddHandler),
]