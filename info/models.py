#coding=utf-8
from django.db import models

from members.models import Member

_cat_choices = (('w', '文字'),('p','图片'),('v','视频'))

class Info(models.Model):
	name = models.CharField( '名称', max_length = 64, blank = True )
	url = models.CharField( '路径', blank = True, max_length = 128 )
	words = models.CharField( verbose_name = '描述', blank = True, max_length = 255 )
	user = models.ForeignKey( Member, verbose_name = '用户' )
	cat = models.CharField( '类型', max_length = 3, choices = _cat_choices )
	createtime = models.DateTimeField( auto_now_add = True, verbose_name = '创建时间' )

	class Meta:
		verbose_name = '状态'
		verbose_name_plural = '状态'

	def __unicode__(self):
		return self.get_cat_display()
