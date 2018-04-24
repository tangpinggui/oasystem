# coding=utf-8
from models.files.upload_file_model import  (
    Files, FilesToUser, DelFilesToUser,
)
from uuid import uuid4
from datetime import datetime


def get_files_lib(self, page):
    ''' 获取所有文件 '''
    files = Files.all()
    return files

def upload_files_lib(self, upload_files):
    ''' 文件的存储 '''
    file_path = []
    for upload_file in upload_files:
        result = save_file(self, upload_file)
        file_path.append(result)
    return file_path if file_path else None

def save_file(self, upload_file):
    files_ext = upload_file['filename'].split('.')[-1]
    if files_ext not in ['jpg', 'bmp', 'png', 'ogg', 'mp3', 'mp4']:
        return {'status': False, 'msg': ' 不支持该格式'}

    uuidname = str(uuid4()) + '.{}'.format(files_ext)
    file_content = upload_file['body']
    old_file = Files.file_is_existed(file_content)
    if old_file is not None:
        file_path = 'http://127.0.0.1:8000/images/' + old_file.uuid
        return {'status': True, 'msg': '文件保存成功(其实以前有人上传过了)', 'data': file_path}

    path = 'files/' + uuidname
    with open(path, 'wb') as f:
        f.write(file_content)

    file = Files()
    file.filename = upload_file['filename']
    file.content_length = len(file_content)
    file.uuid = uuidname
    file.content_type = upload_file['content_type']
    file.update_time = datetime.now()
    file.file_hash = file_content

    file.files_users.append(self.current_user)

    self.db.add(file)
    self.db.commit()
    file_path = 'http://127.0.0.1:8000/images/' + file.uuid
    return {'status': True, 'msg': '文件保存成功','data': file_path}


def files_message_lib(self, file_uuid):
    ''' 显示文件返回文件 '''
    files = Files.by_uuid(file_uuid)
    return files

def file_page_lib(self, page):
    ''' 返回分页的关键数据
        :page 当前页 u'1'
     '''
    files = self.current_user.user_files
    files_page = get_page_list(int(page), files, 2)
    files_del = self.current_user.user_files_del
    return files_page['files'], files_page, files_del

def get_page_list(current_page, content, MAX_PAGE):
    ''' 根据文件篇数分页 （每页假如放10个file）
        ：current_page 当前页
        ：contetn [ 文件 ] type:list
        ：MAX_PAGE  一页分多少个文件数
    '''
    start = (current_page - 1) * MAX_PAGE  # 第一页：1-1=0 第二页：2-1*10=10
    end = start + MAX_PAGE # 第一页：0+10     第二页：10+10=20
    # 切片从索引0
    split_contetn = content[start:end] # 100file  每页10 第一页1-10  2：11-20
    # 文件总数量
    total = content.count()
    # 总共分为页数
    count = total / MAX_PAGE
    if total % MAX_PAGE != 0:
        count += 1
    # 上一页
    pre_page = current_page - 1
    # 下一页
    next_page = current_page + 1
    if pre_page == 0:
        pre_page = count
    if next_page > count:
        next_page = count

    if count < 5:
        pages = [page for page in xrange(1, count+1)]
    elif current_page <= 3:
        pages = [page for page in xrange(1, 6)]
    elif current_page >= count - 2:
        pages = [page for page in xrange(count - 4, count + 1)]
    else:
        pages = [page for page in xrange(count - 2, count + 3)]
    return {
        'files': split_contetn,
        'count': count,
        'pre_page': pre_page,
        'next_page': next_page,
        'current_page': current_page,
        'pages': pages,
    }