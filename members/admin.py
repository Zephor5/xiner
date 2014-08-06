#coding=utf-8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from models import Location,Member

class  LocationAdmin(admin.ModelAdmin):
    list_display = ('city', 'country')

admin.site.register(Location, LocationAdmin)

# Define an inline admin descriptor for Member model
# which acts a bit like a singleton
class MemberInline(admin.StackedInline):
    model = Member
    can_delete = False
    verbose_name_plural = 'member'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (MemberInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
