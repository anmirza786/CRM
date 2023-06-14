from django.contrib import admin
from accounts.models import UserAccount


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'name',
        'is_active',
    ]


admin.site.register(UserAccount, UserAdmin)
