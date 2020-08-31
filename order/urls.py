from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    path('order_create/', views.order_create, name='order_create'),
    path('order_done/', views.done, name='order_done')
]
