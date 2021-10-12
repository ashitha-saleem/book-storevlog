from django.urls import path
from . import views
urlpatterns = [

    path('register', views.reg, name='register'),
    path('login/', views.log, name='lg'),

    path('logout', views.logout, name='logout'),

]
