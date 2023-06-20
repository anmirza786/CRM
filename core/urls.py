from django.contrib.auth import views as auth_views
from django.urls import path
from core import views

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', views.login, name='login'),
    path('auth/<int:data>/', views.auth_conf, name='auth'),
    path('', views.home, name='home'),
    path('welcome/', views.welcome, name='welcome'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('settings/', views.settings, name='settings'),
    path('settings/users/', views.user_listing, name='users'),
    path('settings/users/add-user/', views.add_user, name='add-user'),
    path('settings/users/delete-user/<int:pk>/',
         views.delete_user, name='delete-user'),
    path('settings/users/edit-user/<int:pk>/',
         views.edit_user, name='edit-user'),
    path('settings/roles/', views.roles_listing, name='roles'),
    path('reset-password/', views.password_reset, name='password_reset'),
    path('reset-password/confirm/', views.password_reset_confirm,
         name='password_reset_confirm'),

]
