from django.contrib import admin

from .models import User
from baskets.admin import BasketAdminInLine


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (BasketAdminInLine, )