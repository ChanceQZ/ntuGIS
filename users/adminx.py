import xadmin
from xadmin import views

from .models import Member

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSetting(object):
    site_title = "GIS工作室后台管理系统"
    site_footer = "南通大学地理科学学院GIS工作室"
    menu_style = "accordion"


class MemberAdmin(object):
    list_display = ['name', 'gender', 'image', 'info']
    search_fields = ['name', 'gender', 'image', 'info']
    list_filter = ['name', 'gender', 'image', 'info']




xadmin.site.register(Member, MemberAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)