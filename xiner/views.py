#coding=utf-8
from django.core import serializers
from django.shortcuts import render,redirect
from info.models import Info

from utils import _info_relation

def index(request):
    context = {
        # 'posts':serializers.serialize('json', Info.objects.order_by('-createtime')[:5], indent=4, relations=_info_relation)
    }
    return render(request, 'index.html', context)

def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')
    else:
        import pytz
        return render(request, 'set_timezone.html', {'timezones': pytz.common_timezones})
