from django.db import models


class RolesENUM(models.IntegerChoices):
    ADMIN = 1, 'Admin User'
    INDIVIDUALS = 3, 'Archived Competitions'


class Role(models.Model):
    name = models.CharField(max_length=10,
                            blank=False, null=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
