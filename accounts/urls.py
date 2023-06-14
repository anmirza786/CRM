from django.contrib.auth import views as auth_views
from django.urls import path
from accounts import views

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', views.login, name='login'),
    path('auth/<int:data>/', views.auth_conf, name='auth'),
    path('welcome/', views.welcome, name='welcome'),
]
