from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, get_user_model
from accounts.models import AuthCode
from datetime import date

today = date.today()

User = get_user_model()


def auth_conf(request, data):
    user = User.objects.get(id=data)
    if request.method == 'POST':
        code = request.POST.get('code')
        auth = AuthCode.objects.filter(
            user_id=user.id, code=code, created_at=today, is_used=False).first()
        if auth is not None:
            auth.is_used = True
            auth.save()
            auth_login(request, user)
            return redirect('welcome')
        else:
            return redirect('auth', user=user)
    return render(request, 'auth_conf.html')


def welcome(request):
    return render(request, 'welcome.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('welcome')

    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            if AuthCode.objects.filter(user=user, created_at=today, is_used=False).count() < 3:
                code = AuthCode.objects.create(user=user)
                code.send_two_factor_email()
                return redirect('auth', data=user.id)
            else:
                error_message = 'To Many Login Attempts.'
                return render(request, 'login.html', {'error_message': error_message})
        else:
            error_message = 'Invalid username or password.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
