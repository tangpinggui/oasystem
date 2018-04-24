# coding=utf-8
from handlers.base.base_handler import BaseHandler
from libs.files import files_libs


class FilesListHandler(BaseHandler):
    ''' 文件展示 '''
    def get(self, page):
        files = files_libs.get_files_lib(self, page)

        return self.render('files/files_list.html', files=files)


class FilesUploadHandler(BaseHandler):
    ''' 上传文件 '''
    def get(self):
        self.render('files/files_upload.html')

    def post(self):
        upload_files = self.request.files.get('importfile', '')
        result = files_libs.upload_files_lib(self, upload_files)
        if result is None:
            return self.write({'status':400, 'msg': '有错误'})
        return self.write({'status': 200, 'msg': '保存成功', 'data': result})


class FilesMessageHandler(BaseHandler):
    ''' 显示文件列表 '''
    def get(self):
        file_uuid = self.get_argument('uuid', '')
        files = files_libs.files_message_lib(self, file_uuid)
        kw = {
            'files': files,
        }
        self.render('files/files_message.html', **kw)


class FilesPageListHandler(BaseHandler):
    ''' 分页列表 '''
    def get(self, page):
        print page # 1 当前页
        print type(page)
        files, files_page, files_del = files_libs.file_page_lib(self, page)
        kw = {
            'files': files,
            'files_page': files_page,
            'files_del': files_del,
        }
        self.render('files/files_page_list.html', **kw)