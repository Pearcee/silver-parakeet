from django.urls import path
from . import views
urlpatterns = [
    path(r'', views.index,name='index'),
    path(r'posts/base_layout',views.base_layout,name='base_layout'),
    path(r'posts/getdata',views.getdata,name='getdata')
]