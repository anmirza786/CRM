from django.contrib import admin
from core.models import UserAccount


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'first_name',
        'last_name',
        'is_active',
    ]


admin.site.register(UserAccount, UserAdmin)
