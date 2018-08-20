"""ntuGIS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import xadmin
from information.views import index, survey, project, article_page, newsnews
from users.views import inform


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', index),
    url(r'^survey/$', survey, name='survey'),
    url(r'^inform/$', inform, name='inform'),
    url(r'^project/$', project, name='project'),
    url(r'^article/(?P<article_id>[0-9]+)$', article_page,name='article'),
    url(r'^newsnews/$', newsnews, name='newsnews')
]
