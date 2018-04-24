import article_handler


article_urls = {
    (r'/article/article_list', article_handler.ArticleListHandler),
    (r'/article/add_article', article_handler.AddArticleHandler),
    (r'/article/article', article_handler.ArticleHandler),
    (r'/article/addlike', article_handler.ArticleLikeHandler),
    (r'/article/addcomment', article_handler.ArticleFirstCommentHandler),
    (r'/article/addsecondcomment', article_handler.ArticleSecondCommentHandler),
    (r'/article/article_modify_manage', article_handler.ArticleModifyManageHandler),
    (r'/article/article_modify', article_handler.ArticleModifyHandler),
    (r'/article/article_delete', article_handler.DelArticleHandler),
    (r'/article/add_category_tag', article_handler.AddCategoryTagHandler),
    (r'/article/del_category_tag', article_handler.DelCategoryTagHandler),
}