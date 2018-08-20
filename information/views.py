from django.shortcuts import render
from .models import News, Banner, JiangX
from .models import Introduce
from .models import Honor
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def index(request):
    news1, news2, news3 = News.objects.all().order_by('-id')[0:3]
    ban1, ban2, ban3 = Banner.objects.all().order_by('-id')[0:3]
    jx1, jx2, jx3, jx4 = JiangX.objects.all().order_by('-id')[0:4]
    return render(request, 'index.html', context={
        'news1': news1,
        'news2': news2,
        'news3': news3,
        'ban1' : ban1,
        'ban2' : ban2,
        'ban3' : ban3,
        'jx1': jx1,
        'jx2': jx2,
        'jx3': jx3,
        'jx4': jx4
    })


def survey(request):
    introduce = Introduce.objects.get(id=1)
    return render(request, 'survey.html', context={'introduce': introduce})


def project(request):
    pro_hor = Honor.objects.filter(category='proj')
    inv_hor = Honor.objects.filter(category='invent')
    com_hor = Honor.objects.filter(category='compet')
    paper_hor = Honor.objects.filter(category='paper')
    return render(request, 'project.html', context={
        'pro_hor': pro_hor,
        'inv_hor' : inv_hor,
        'com_hor' : com_hor,
        'paper_hor' : paper_hor
    })


def article_page(request, article_id):
    article = News.objects.get(id=article_id)
    return render(request, 'article_page.html', context={'article': article})


def newsnews(request):
    newinfo = News.objects.all().order_by('-id')
    #对新闻消息进行分页
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(newinfo, 10, request=request)

    newpage = p.page(page)
    return render(request, 'newsnews.html', context={
        'newpage': newpage
    })