from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('main/', views.hi, name='hi'),

]