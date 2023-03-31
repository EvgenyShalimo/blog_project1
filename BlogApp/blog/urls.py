from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('contakts/', views.contakts),
    path('registration/', views.contact),
    path('user_list/', views.list_user),
    path('<int:pk>', views.NewsDetailView.as_view(), name='user_room'),
]