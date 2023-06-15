from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, get_user_model
from core.models import AuthCode
from datetime import date

# get today's date 
today = date.today()

# get user model 
User = get_user_model()

# otp confirmation form 
def auth_conf(request, data):
    user = User.objects.get(id=data)
    if request.method == 'POST':
        code = request.POST.get('code')
        print(code)
        auth = AuthCode.objects.filter(
            user_id=user.id, code=code, created_at=today, is_used=False).first()
        if auth is not None:
            auth.is_used = True
            auth.save()
            auth_login(request, user)
            return redirect('welcome')
        else:
            return redirect('auth', data=user.id)
    return render(request, 'auth_conf.html', {'is_auth_page': True})

# auth successful page 
def welcome(request):
    if request.method == 'POST':
        return redirect('dashboard')
    return render(request, 'redirect-to-dashboard.html')

# login page
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
                return render(request, 'login.html', {'error_message': error_message, 'is_auth_page': True})
        else:
            error_message = 'Invalid username or password.'
            return render(request, 'login.html', {'error_message': error_message, 'is_auth_page': True})
    else:
        return render(request, 'login.html', {'is_auth_page': True})
