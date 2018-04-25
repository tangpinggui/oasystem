# coding=utf-8
from qiniu import Auth, put_data


access_key ='mhQj0QrtJ-APGgkVzd---zLYm3s_9OhIwOdLtiEC'
secret_key ='BcjyMsjqG4XMfNuyNqxhRCFn8oBBXX5DAdT7hijo'
bucket_name ='rock1'


def upload_qiniu_file_content(content):
    q = Auth(access_key, secret_key)
    token = q.upload_token(bucket_name)

    ret, info = put_data(token, None, content)
    return ret['key'], info