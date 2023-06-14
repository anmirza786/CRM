from django.contrib import admin
from accounts.models import Role


# Register your models here.
class RoleAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]


admin.site.register(Role, RoleAdmin)
