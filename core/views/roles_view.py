from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.http import JsonResponse
from core.forms import CustomUserCreationForm, CustomUserEditForm
from core.forms.role_creation_form import RoleCreationForm
from core.models import Role
from core.utils import get_users_count
User = get_user_model()


def roles_listing(request):
    roles = Role.objects.all()
    newRoles = []
    for role in roles:
        singleRole = {
            'id': role.id,
            'name': role.name,
            'description': role.description,
            'count': User.objects.filter(role_id=role.id).count()
        }
        newRoles.append(singleRole)
    context = {
        'roles': newRoles,
    }
    return render(request, 'roles.html', context)


def add_roles(request):
    form = RoleCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            errors = form.errors
    else:
        form = RoleCreationForm()

    return render(request, 'roles_form/add_role_form.html', {'form': form})


def edit_role(request, pk):
    user = User.objects.get(id=pk)
    form = CustomUserEditForm(request.POST, instance=user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            errors = form.errors
    else:
        form = CustomUserEditForm(instance=user)

    return render(request, 'users_form/edit_user_form.html', {'form': form})


def delete_role(request, pk):
    user = User.objects.get(id=pk)
    deleted = user.delete()
    if deleted:
        return redirect('users')
