from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.http import JsonResponse
from core.forms import CustomUserCreationForm, CustomUserEditForm

User = get_user_model()

# dashboard url wuth the login required devorator


@login_required
def home(request):
    return redirect('dashboard')


@login_required
def dashboard(request):

    return render(request, 'dashboard.html')


def settings(request):
    return render(request, 'settings.html')


def user_listing(request):
    my_model = User.objects.all()
    if request.method == 'POST':
        page_n = request.POST.get('page_n', None)
        page_size = request.POST.get('size', None)
        if page_n is not None and page_size is not None:
            paginatorr = Paginator(my_model, page_size)
            results = list(paginatorr.page(
                page_n).object_list.values('id', 'first_name', 'last_name', 'email', 'role__name', 'role', 'is_active'))
            users = paginatorr.page(page_n)
            has_next = users.has_next()
            has_previous = users.has_previous()
            next_page_number = users.next_page_number() if has_next else None
            num_pages = users.paginator.num_pages
            numbers = users.number
            page_range = list(users.paginator.page_range)
            previous_page_number = users.previous_page_number() if has_previous else None
            context = {
                'has_next': has_next,
                'has_previous': has_previous,
                'next_page_number': next_page_number,
                'num_pages': num_pages,
                'current_page_number': numbers,
                'page_range': page_range,
                'previous_page_number': previous_page_number
            }
        else:
            paginatorr = Paginator(my_model, page_size)
            results = list(paginatorr.page(1).object_list.values(
                'id', 'first_name', 'last_name', 'email', 'role__name', 'role', 'is_active'))
            users = paginatorr.page(1)
            has_next = users.has_next()
            has_previous = users.has_previous()
            next_page_number = users.next_page_number() if has_next else None
            num_pages = users.paginator.num_pages
            numbers = users.number
            page_range = list(users.paginator.page_range)
            previous_page_number = users.previous_page_number() if has_previous else None
            context = {
                'has_next': has_next,
                'has_previous': has_previous,
                'next_page_number': next_page_number,
                'num_pages': num_pages,
                'current_page_number': numbers,
                'page_range': page_range,
                'previous_page_number': previous_page_number
            }

        return JsonResponse({"results": results, 'context': context})
    else:
        number_of_item = 2
        paginatorr = Paginator(my_model, number_of_item)
        first_page = paginatorr.page(1).object_list
        page_range = paginatorr.page_range
        hasPrevios = paginatorr.page(1).has_previous
        hasNext = paginatorr.page(1).has_next
        users = paginatorr.page(1)

        context = {
            'users': users,
            'has_previos': hasPrevios,
            'has_next': hasNext,
            'first_page': first_page,
            'page_range': page_range,
            'page_size': number_of_item
        }

    return render(request, 'users.html', context)


def add_user(request):
    form = CustomUserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            errors = form.errors
    else:
        form = CustomUserCreationForm()

    return render(request, 'users_form/add_user_form.html', {'form': form})


def edit_user(request, pk):
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


def delete_user(request, pk):
    user = User.objects.get(id=pk)
    deleted = user.delete()
    if deleted:
        return redirect('users')
