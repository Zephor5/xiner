from django.contrib import admin
from models import Info

class InfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'words', 'url', 'cat', 'createtime')

    def save_model(self, request, obj, form, change):
		obj.user = request.user.member
		obj.save()

admin.site.register(Info, InfoAdmin)