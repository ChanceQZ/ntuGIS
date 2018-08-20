from datetime import datetime

from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=50, verbose_name=u"标题", default="")
    content = models.TextField(max_length=1000, verbose_name=u"内容", default="")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    image = models.ImageField(upload_to="static/image/news/%Y/%m", max_length=100, default="")

    class Meta:
        verbose_name = "最新消息"
        verbose_name_plural = verbose_name


class Honor(models.Model):
    date = models.CharField(max_length=30, verbose_name=u"获得时间", default="")
    name = models.CharField(max_length=100, verbose_name=u"奖项名称", default="")
    category = models.CharField(max_length=20, verbose_name=u"种类",  choices=(("compet", u"竞赛"),("proj",u"项目"),
                                ("invent",u"发明"),("paper",u"论文")),default="compet")
    members = models.CharField(max_length=200, verbose_name=u"团队成员", default="")
    place = models.CharField(max_length=200, verbose_name=u"授予单位", default="")
    grade = models.CharField(max_length=200, verbose_name=u"级别",choices=((u"国家级", u"国家级"),(u"省级", u"省级"),
                                (u"校级", u"校级")), default=u"国家级")

    class Meta:
        verbose_name = "团队荣誉"
        verbose_name_plural = verbose_name


class Introduce(models.Model):
    intro = models.CharField(max_length=500, verbose_name=u"介绍", default="")
    dream = models.CharField(max_length=500, verbose_name=u"愿景", default="")
    team = models.CharField(max_length=500, verbose_name=u"团队", default="")
    image = models.ImageField(upload_to="static/image/%Y/%m", max_length=100)

    class Meta:
        verbose_name = "工作室概况"
        verbose_name_plural = verbose_name

class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(upload_to="static/image/banner/%Y/%m", verbose_name=u"轮播图", max_length=100)
    addtime = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

class JiangX(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(upload_to="static/image/JiangX/%Y/%m", verbose_name=u"轮播图", max_length=100)
    addtime = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"奖项轮播图"
        verbose_name_plural = verbose_name