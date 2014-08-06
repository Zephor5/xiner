#coding=utf-8
import json
from django.core import serializers
from django.db import connection
from django.shortcuts import render,redirect
from members.models import Member
from info.models import Info

_info_relation = {
        'user':{
            'relations':{
                'user':{
                    'fields':('username',)#'first_name','last_name','email','last_login')
                }
            },
            'fields':('user',)
        }
    }

def index(request):
    context = {
        'posts':serializers.serialize('json', Info.objects.order_by('-createtime'), indent=4, relations=_info_relation)
    }
    return render(request, 'index.html', context)

def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')
    else:
        import pytz
        return render(request, 'set_timezone.html', {'timezones': pytz.common_timezones})
