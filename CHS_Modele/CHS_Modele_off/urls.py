from django.urls import path
from . import views

urlpatterns = [

    path('', views.chs_dash, name='chs_dash'),
    path('create/', views.create_chs, name='create_chs'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_user, name='logout_user'),


]