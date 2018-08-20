import xadmin

from .models import News, Honor, Introduce, Banner, JiangX


class NewsAdmin(object):
    list_display = ['title', 'content', 'image', 'add_time']
    search_fields = ['title', 'content', 'image']
    list_filter = ['title', 'content', 'image', 'add_time']


class HonorAdmin(object):
    list_display = ['date', 'name', 'members', 'place', 'category', 'grade']
    search_fields = ['date', 'name', 'members', 'place', 'category', 'grade']
    list_filter = ['date', 'name', 'members', 'place', 'category', 'grade']

class IntroduceAdmin(object):
    list_display = ['intro', 'dream', 'team', 'image']
    search_fields = ['intro', 'dream', 'team', 'image']
    list_filter = ['intro', 'dream', 'team', 'image']


class BannerAdmin(object):
    list_display = ['title', 'image', 'addtime']
    search_fields = ['title', 'image']
    list_filter = ['title', 'image', 'addtime']


class JiangXAdmin(object):
    list_display = ['title', 'image', 'addtime']
    search_fields = ['title', 'image']
    list_filter = ['title', 'image', 'addtime']
xadmin.site.register(News, NewsAdmin)
xadmin.site.register(Honor, HonorAdmin)
xadmin.site.register(Introduce, IntroduceAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(JiangX, JiangXAdmin)