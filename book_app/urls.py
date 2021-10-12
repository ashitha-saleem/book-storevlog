from django.urls import path
from . import views
app_name='myapp'
urlpatterns = [

    # path('tours/',views.hoom,name='hoom'),
    path('',views.demo,name='demo'),
    path('market/<int:shop_id>',views.details,name='details'),
    path('add/',views.ad,name='ad'),
    # path('register', views.reg, name='register'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>', views.delete, name='delete'),


]
