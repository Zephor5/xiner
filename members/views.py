from django.shortcuts import render
from members.models import Member

def all(request):
	return render(request, 'members/all.html')
