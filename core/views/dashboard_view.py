from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# dashboard url wuth the login required devorator


@login_required
def dashboard(request):

    return render(request, 'dashboard.html')
