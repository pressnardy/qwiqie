from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.account, name='account'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('success/<str:message>', views.first_login, name='first_login'),
    path('terms/', views.terms, name='terms'),
    
]

