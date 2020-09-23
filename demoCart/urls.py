from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name='main'),
    path('<int:catalog_id>/desktops', views.desktops, name='desktops')
]
