# coding=utf-8
from models.article.article_model import (
    Article, ArticleToTag, UserLikeArticle, Category,Comment,SecondComment, Tag
)



def article_list_lib(self):
    ''' 显示文档首页 需要的数据'''
    articles = Article.all_createtime_desc()
    comments = Comment.all_createtime_desc()
    # tags = Tag.all()
    # categorys = Category.all()
    tags, categorys = get_tags_categorys_lib(self)
    return articles, comments, categorys, tags

def get_tags_categorys_lib(self):
    ''' 上传文章 的页面需要的数据 '''
    tags = Tag.all()
    categorys = Category.all()
    return tags, categorys

# def add_article_lib(self, title, article, desc, category_id, thumbnail, tags):
#     if category_id == '' or tags == '':
#         return {'status': False, 'msg': '分内和标签很重要'}
#
#     if title == '' or article == '' or desc == '':
#         return {'status': False, 'msg': '请输入标题，内容，简介'}
#
#     article = Article()
#     article.content = article
#     article.title = title
#     article.desc = desc
#     article.category_id = category_id
#     article.thumbnail = thumbnail
#
#     for tag_id in tags:
#         tag = Tag.by_id(tag_id)
#         article.tags.append(tag)
#
#     article.user_id = self.current_user.id
#     self.db.add(article)
#     self.db.commit()
#
#     return {'status': True, 'msg': '文档提交成功'}
def add_article_lib(self, title, content, desc, category_id, thumbnail, tags, article_id):
    ''' 上传文章  及修改文章 '''
    if category_id == '' or tags == '':
        return {'status':False, 'msg':'请选择分类或者标签'}

    if title == '' or content=='' or desc == '':
        return {'status': False, 'msg': '请输入标题，内容， 简介'}

    if article_id != '':
        print '2-'*19
        article = Article.by_id(article_id)
        article.tags = []

    else:
        print '-1-'*10
        article = Article()
    article.content = content
    article.title = title
    article.desc = desc
    article.category_id = category_id
    article.thumbnail = thumbnail

    for tags_id in tags:
        tag = Tag.by_id(tags_id)
        article.tags.append(tag)

    article.user_id = self.current_user.id
    self.db.add(article)
    self.db.commit()
    if article_id != '':
        return {'status': True, 'msg': '文档修改成功'}
    return {'status': True, 'msg': '文档提交成功'}

def article_lib(self, article_id):
    ''' 显示文章详情页 '''
    article = Article.by_id(article_id)
    comments = article.comments

    return article, comments

def add_article_like_lib(self, article_id):
    ''' 点赞与取消点赞 '''
    article = Article.by_id(article_id)
    if article is None:
        return {'status': False, 'msg': '该文章不存在'}
    if self.current_user in article.user_likes:
        article.user_likes.remove(self.current_user)
        self.db.add(article)
        self.db.commit()
        return {'status': True, 'msg': '取消了点赞'}
    article.user_likes.append(self.current_user)
    self.db.add(article)
    self.db.commit()
    return {'status': True, 'msg': '点赞成功'}

def comment_content_lib(self, comment_content, article_id):
    ''' 一级评论内容存储 '''
    if comment_content == '':
        return {'status': False, 'msg': '评论不能为空'}
    article = Article.by_id(article_id)
    if article is None:
        return {'status': False, 'msg': '文章不存在'}
    comment = Comment()
    comment.content = comment_content
    comment.article_id = article_id
    comment.user_id = self.current_user.id
    self.db.add(comment)
    self.db.commit()
    return {'status': True, 'msg': '评论成功'}

def second_comment_content_lib(self, comment_content, first_comment_id):
    ''' 二级评论内容存储 '''
    if comment_content == '':
        return {'status': False, 'msg': '评价不能为看'}
    first_comment = Comment.by_id(first_comment_id)
    if first_comment is None:
        return {'status': False, 'msg': '评价的评论已不存在'}

    second_comment = SecondComment()
    second_comment.content = comment_content
    second_comment.comment_id = first_comment_id
    second_comment.user_id = self.current_user.id
    self.db.add(second_comment)
    self.db.commit()
    return {'status': True, 'msg': '附加评论成功'}

def get_articles():
    ''' 返回所有文章给修改文章的主页 '''
    articles = Article.all()

    return articles

def get_article_things(self, article_id):
    ''' 修改的文章的详细 '''
    article = Article.by_id(article_id)
    tags, categorys = get_tags_categorys_lib(self)

    return article, categorys, tags

def del_article_lib(self, article_id):
    ''' 删除文章 '''
    article = Article.by_id(article_id)
    if article is None:
        return {'status': False, 'msg': '文章已经不存在'}
    self.db.delete(article)
    self.db.commit()
    # articles = Article.all()
    return {'status': True}

def add_category_tag_lib(self, category_name='', tag_name=''):
    ''' 添加文章的分类和标签 '''
    if category_name != '':
        category = Category.by_name(category_name)
        if category== None:
            category = Category()
            category.name = category_name
            self.db.add(category)
            self.db.commit()
    if tag_name != '':
        tag = Tag.by_name(tag_name)
        if tag == None:
            tag = Tag()
            tag.name = tag_name
            self.db.add(tag)
            self.db.commit()
    return {'status': True}

def  del_category_tag_lib(self, category_uuid, tag_uuid):
    ''' 删除分类，标签 '''
    category = Category.by_uuid(category_uuid)
    tag = Tag.by_uuid(tag_uuid)
    if category != None:
        self.db.delete(category)
    if tag != None:
        self.db.delete(tag)
    self.db.commit()
    return {'status': True}




