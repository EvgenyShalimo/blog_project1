from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_user, name='list_users'),
    path('contakts/', views.contakts, name='contacts'),
    path('registration/', views.contact, name='registration'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='user_room'),
]