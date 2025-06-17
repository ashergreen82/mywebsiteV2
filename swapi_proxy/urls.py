from django.urls import path, re_path
from . import views

urlpatterns = [
    path('people/', views.search_people, name='search_people'),
    # Catch-all pattern for other SWAPI resources (e.g., planets/1/, species/1/, etc.)
    re_path(r'^(?P<path>.*?)/?$', views.proxy_swapi, name='proxy_swapi'),
]
