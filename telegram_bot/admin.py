from django.contrib import admin
from .models import User, UserStatistic


@admin.register(User)
class Log(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.get_fields()]
    list_filter = ("created_at", "id", "user_id", "email")
    search_fields = ('user_id', "email", 'tariff')


@admin.register(UserStatistic)
class Log(admin.ModelAdmin):
    list_display = [field.name for field in UserStatistic._meta.get_fields()]
    list_filter = ("id", "user", "type", "name")
    search_fields = ('user', "type", 'name')
