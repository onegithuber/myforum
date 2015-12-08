from django.contrib import admin


# Register your models here.
from forum.models import ForumUser


class ForumUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'nickname')
    list_filter = ('is_active', 'is_staff', 'date_joined')


admin.site.register(ForumUser, ForumUserAdmin)
