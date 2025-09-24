from django.contrib import admin
from polls.models import Choice, Question
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group, User

class CustomAdminSite(admin.AdminSite):
    site_header = "Monty Python Administration"


admin_site = CustomAdminSite()
admin_site.register(Choice)
admin_site.register(Question)
admin_site.register(Group, GroupAdmin)
admin_site.register(User, UserAdmin)