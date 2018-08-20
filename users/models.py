from datetime import datetime

from django.db import models

# Create your models here.


class Member(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"姓名", default="")
    gender = models.CharField(max_length=6, choices=(("male", u"男"),("female",u"女")),
                              default="male", verbose_name=u"性别")
    image = models.ImageField(upload_to="static/image/photo/%Y/%m", max_length=100)
    info = models.CharField(max_length=1000, verbose_name=u"信息", default="")

    class Meta:
        verbose_name = "成员信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

