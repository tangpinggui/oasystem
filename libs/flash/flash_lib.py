# coding=utf-8


def flash(self, message, category='message'):
    """先调用flash"""
    flashes = self.session.get('_flashes', [])
    print '--'*10
    flashes.append((category, message))  #[('error', '保存失败'),('ok', '分类保存了')]
    self.session.set('_flashes', flashes)


def get_flashed_messages(self, with_categories=False, category_filter=[]):
    """后调用get_flashed_messages
     {% for category, message in get_flashed_messages(with_categories=True) %}
     {% if category == 'error' %}

    """
    flashes = self.flashes
    if flashes is None:
        self.flashes = flashes = self.session.get('_flashes', [])
        del self.session['_flashes']
    if category_filter:
        flashes = list(filter(lambda f: f[0] in category_filter, flashes))
    if not with_categories:
        return [x[1] for x in flashes]
    return flashes