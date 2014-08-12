#coding=utf-8
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

from models import Info
from xiner.utils import _info_relation

def json_data(request):
    last_id = request.GET.get('last_id')
    try:
        last_id = int(last_id)
    except:
        return HttpResponse('[]',content_type="application/json")
    if last_id:
        res = serializers.serialize('json', Info.objects.filter(id__lt=last_id).order_by('-createtime')[:5], indent=4, relations=_info_relation)
    else:
    	res=serializers.serialize('json', Info.objects.order_by('-createtime')[:5], indent=4, relations=_info_relation)
    return HttpResponse(res,content_type="application/json")
