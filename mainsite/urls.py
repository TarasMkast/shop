from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'mainsite'
urlpatterns = [
    path('', views.main, name='main'),
    path('all/catalog/', views.all_catalog, name='all_catalog'),
    path('<int:maincatalog_id>/catalog/', views.catalog, name='catalog'),
    path('index/', views.index, name='index')

]
