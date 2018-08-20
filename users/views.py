from django.shortcuts import render
from .models import Member

# Create your views here.

def inform(request):
    zt = Member.objects.get(name="周侗")
    tf = Member.objects.get(name="陶菲")
    ktl = Member.objects.get(name="康天乐")
    fzl = Member.objects.get(name="范紫灵")
    zrj = Member.objects.get(name="张瑞嘉")
    qz = Member.objects.get(name="钱振")
    lj = Member.objects.get(name="陆杰")
    lh = Member.objects.get(name="刘浩")
    cpy = Member.objects.get(name="陈品玉")
    chx = Member.objects.get(name="陈昊烜")
    hyc = Member.objects.get(name="胡宇宸")
    ldh = Member.objects.get(name="刘冬晖")
    return render(request, 'inform.html', context={
        'zt' : zt,
        'tf' : tf,
        'ktl' : ktl,
        'fzl' : fzl,
        'zrj' : zrj,
        'qz' : qz,
        'lj' : lj,
        'lh' : lh,
        'cpy' : cpy,
        'chx' : chx,
        'hyc' : hyc,
        'ldh' : ldh
    })


