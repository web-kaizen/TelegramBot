from django.contrib import admin
from .models import User, UserStatistic


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'email', 'password', 'balance', 'tariff', 'created_at']
    list_filter = ("created_at", "email")
    search_fields = ('user_id', "email", 'tariff')


@admin.register(UserStatistic)
class UserStatisticAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'model_id', 'name', 'current_dialogues', 'max_dialogues']
    list_filter = ("id", "user", "model_id", "name")
    search_fields = ('user', "model_id", 'name')
