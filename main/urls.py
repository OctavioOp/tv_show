from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('new_show', views.create_new_show),
    path('home/delete_show/<id_show>', views.delete_show),
    path('home/edit_show/<id_show>', views.edit_show),
    path('home/show_tv/<tv_id>', views.show_show),
    path('find_show', views.search_show),
    path('home/delete_by_ajax/<id_show>', views.delete_by_ajax)
]
