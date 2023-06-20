from django.contrib.auth import get_user_model
User = get_user_model()


def get_users_count(role_id):
    users_count = User.objects.filter(role_id=role_id).count()
    return users_count
