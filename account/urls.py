from django.urls import path
from account import views
app_name='account'
urlpatterns = [
    path('regist/', views.regist, name='regist'),
    path('registlogic/', views.registlogic, name='registlogic'),
    path('login/', views.login, name='login'),
    path('loginlogic/', views.loginlogic, name='loginlogic'),
    path('home/', views.home, name='home')
]