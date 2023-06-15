from django.core.management.base import BaseCommand
from core.models import Role

Roles_Seeder = [
    {
        "name": "Global Administrator"
    },
    {
        "name": "Support"
    },
    {
        "name": "Sales"
    },
    {
        "name": "Client"
    },
    {
        "name": "Doctor"
    },
    {
        "name": "Affiliate"
    },
]


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for Data in Roles_Seeder:
            Role.objects.create(name=Data['name'])
