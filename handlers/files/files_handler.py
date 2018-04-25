# coding=utf-8
from handlers.base.base_handler import BaseHandler
from libs.files import files_libs


class FilesListHandler(BaseHandler):
    ''' 文件展示 '''
    def get(self, page):
        page = page
        files = files_libs.get_files_lib(self, page)

        return self.render('files/files_list.html', files=files)

class FilesDelHandler(BaseHandler):

    def get(self):
        uuid = self.get_argument('uuid', '')
        result = files_libs.del_file(self, uuid)
        return self.redirect('/files/files_page_list/1')


class FilesUploadHandler(BaseHandler):
    ''' 上传文件 '''
    def get(self):
        self.render('files/files_upload.html')

    def post(self):
        upload_files = self.request.files.get('importfile', '') # [{'body': 'aaa', 'content_type': u'text/plain, 'filename':x.py}]
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


class FilesUploadQiniuHandler(BaseHandler):
    """03文件上传到七牛服务器"""
    def get(self):
        self.render('files/files_upload.html')

    def post(self):
        upload_files =self.request.files.get('importfile', None)
        result = files_libs.upload_files_qiniu_lib(self, upload_files)
        if result is None:
            return self.write({'status': 400, 'msg': '有错误了'})
        return self.write({'status': 200, 'msg': '有错误了','data': result})


class FilesDownLoadQiniuHandler(BaseHandler):
    """04从七牛服务器下载文件"""
    def get(self):
        uuid =self.get_argument('uuid', '')
        result = files_libs.files_download_qiniu_lib(self, uuid)
        if result['status'] is True:
            return self.redirect(result['data'])
        else:
            return self.write(result['msg'])


import tornado.gen
from concurrent.futures import ThreadPoolExecutor
executor_g = ThreadPoolExecutor(50)


#重点掌握
class FilesDownLoadHandler(BaseHandler):
    executor = executor_g
    @tornado.gen.coroutine
    def get(self):
        uuid = self.get_argument('uuid', '')
        yield files_libs.files_download_lib(self, uuid)
