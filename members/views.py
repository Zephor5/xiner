#coding=utf-8
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from models import Member

from xiner.utils import _member_relation

def all(request):
	return render(request, 'members/all.html')

def json_data(request):
	res = serializers.serialize('json',Member.objects.all(),indent=4,relations=_member_relation)
	return HttpResponse(res,content_type="application/json")
