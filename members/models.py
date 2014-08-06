#coding=utf-8
from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
	city = models.CharField( max_length = 50, verbose_name = '城市' )
	country = models.CharField( max_length = 50, verbose_name = '国家' )

	class Meta:
		verbose_name = '坐标'
		verbose_name_plural = '坐标'

	def __unicode__(self):
		return "%s·%s"%(self.country,self.city)

class Member(models.Model):
	user = models.OneToOneField(User)
	phone = models.CharField( max_length = 15, null = True, verbose_name = '电话' )
	weichat = models.CharField( max_length = 20, null = True, verbose_name = '微信' )
	location = models.ForeignKey( Location, null = True, verbose_name = '坐标' )

	class Meta:
		verbose_name = '成员信息'
		verbose_name_plural = '成员信息'

	def __unicode__(self):
		return "%s%s(%s)"%(self.user.last_name,self.user.first_name,self.location)
