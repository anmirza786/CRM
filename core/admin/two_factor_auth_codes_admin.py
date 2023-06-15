from django.contrib import admin
from core.models import AuthCode


# Register your models here.
class AuthCodesAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'code',
        'created_at',
        'user',
        'is_used',
    ]


admin.site.register(AuthCode, AuthCodesAdmin)
