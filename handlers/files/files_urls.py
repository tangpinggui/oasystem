# coding=utf-8
import files_handler


files_urls = [
    (r'/files/files_list/(\d{1,3})', files_handler.FilesListHandler),
    (r'/files/files_up_load', files_handler.FilesUploadHandler),
    (r'/files/files_upload', files_handler.FilesUploadHandler),
    (r'/files/files_message', files_handler.FilesMessageHandler),
    (r'/files/files_page_list/(\d{1,3})', files_handler.FilesPageListHandler),  # 不能空格re {}
]