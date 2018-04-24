# coding=utf-8
import json
from handlers.base.base_handler import BaseHandler
from libs.article import article_libs


class ArticleListHandler(BaseHandler):
    ''' 显示文档首页 '''
    def get(self):
        articles, comments, categorys, tags = article_libs.article_list_lib(self)
        kw = {
            'articles': articles,
            'newarticles': articles[:3],
            'newcomments': comments[:3],
            'categorys': categorys,
            'tags': tags,
        }

        self.render('article/article_list.html', **kw)


class AddArticleHandler(BaseHandler):
    ''' 上传文章 '''
    def get(self):
        tags, categorys = article_libs.get_tags_categorys_lib(self)
        kw = {
            'categorys': categorys,
            'tags': tags,
        }

        self.render('article/add_article.html', **kw)

    def post(self):
        title = self.get_argument('title', '')
        article = self.get_argument('article', '')
        desc = self.get_argument('desc', '')
        category = self.get_argument('category', '')
        thumbnail = self.get_argument('thumbnail', '')
        tags = json.loads(self.get_argument('tags', ''))

        article_id = self.get_argument('article_id', '')

        result = article_libs.add_article_lib(self, title, article, desc, category, thumbnail, tags, article_id)
        if result['status'] is True:
            return self.write({'status': 200, 'msg': result['msg']})
        return self.write({'status': 400, 'msg': result['msg']})


class ArticleHandler(BaseHandler):
    ''' 显示文章详情页 '''
    def get(self):
        article_id = self.get_argument('id', '')
        article, comments = article_libs.article_lib(self, article_id)
        kw = {
            'article': article,
            'comments': comments,
        }

        self.render('article/article.html', **kw)


class ArticleLikeHandler(BaseHandler):
    ''' 点赞与取消点赞 '''
    def post(self):
        article_id = self.get_argument('article_id', '')
        result =article_libs.add_article_like_lib(self, article_id)
        if result['status'] is True:
            return self.write({'status': 200, 'msg': result['msg']})
        return self.write({'status': 400, 'msg': result['msg']})


class ArticleFirstCommentHandler(BaseHandler):
    '''文章一级评论 Ajax返回的数据'''
    def post(self):
        comment_content = self.get_argument('content', '')
        article_id = self.get_argument('id', '')
        result =article_libs.comment_content_lib(self, comment_content, article_id)
        if result['status'] is True:
            return self.write({'status': 200, 'msg': result['msg']})
        return self.write({'status': 400, 'msg': result['msg']})


class ArticleSecondCommentHandler(BaseHandler):
    ''' 二级评论 ajax请求 '''
    def post(self):
        first_comment_id = self.get_argument('id', '')
        comment_content = self.get_argument('content', '')
        result =article_libs.second_comment_content_lib(self, comment_content, first_comment_id)
        if result['status'] is True:
            return self.write({'status': 200, 'msg': result['msg']})
        return self.write({'status': 400, 'msg': result['msg']})


class ArticleModifyManageHandler(BaseHandler):
    ''' 修改文章的主页 '''
    def get(self):
        articles = article_libs.get_articles()
        kw = {
            'articles': articles,
        }
        self.render('article/article_modify_manage.html', **kw)


class ArticleModifyHandler(BaseHandler):
    '''   修改指定的文章 '''
    def get(self):
        article_id = self.get_argument('id', '')
        article, categorys, tags = article_libs.get_article_things(self, article_id)
        kw = {
            'article': article,
            'tags': tags,
            'categorys': categorys
        }
        self.render('article/article_modify.html', **kw)


class DelArticleHandler(BaseHandler):
    ''' 删除文章 '''
    def get(self):
        article_id = self.get_argument('id', '')
        result = article_libs.del_article_lib(self, article_id)

        # articles = article_libs.del_article_lib(self, article_id)
        # kw = {
        #     'articles': articles,
        # }
        # self.render('article/article_modify_manage.html', **kw)
        if result['status'] is True:
            return self.redirect('/article/article_modify_manage')
        return self.write(result['msg'])


class AddCategoryTagHandler(BaseHandler):
    ''' 新增加分类和标签 '''
    def get(self):
        tags, categorys = article_libs.get_tags_categorys_lib(self)
        kw = {
            'tags': tags,
            'categorys': categorys
        }
        self.render('article/article_add_category_tag.html', **kw)
    def post(self):
        category_name = self.get_argument('category_name', '')
        tag_name = self.get_argument('tag_name', '')
        article_libs.add_category_tag_lib(self, category_name, tag_name)

        self.redirect('/article/add_category_tag')


class DelCategoryTagHandler(BaseHandler):
    ''' 删除分类，标签 '''
    def get(self):
        tag_uuid = self.get_argument('t_uuid', '')
        category_uuid = self.get_argument('c_uuid', '')
        article_libs.del_category_tag_lib(self, category_uuid, tag_uuid)
        self.redirect('/article/add_category_tag')