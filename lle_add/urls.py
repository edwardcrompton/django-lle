from django.urls import include, path
from . import views

urlpatterns = [
    path('search/', views.search_place, name='search-place'),
    path('place/', views.add_place, name='add-place'),
]