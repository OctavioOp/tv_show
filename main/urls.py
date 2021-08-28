from django.urls import path
from . import views
urlpatterns = [
    path('', views.signup),
    path('signup', views.signup),
    path('login', views.login),
    path('logout', views.logout),
    path('shows/', views.home),
    path('new_show', views.create_new_show),
    path('shows/delete_show/<id_show>', views.delete_show),
    path('shows/edit_show/<id_show>', views.edit_show),
    path('shows/show_tv/<tv_id>', views.show_show),
    path('find_show', views.search_show),
    path('shows/delete_by_ajax/<id_show>', views.delete_by_ajax)
]
