from django.urls import path
from .views import shorten_url, redirect_to_original, url_list

urlpatterns = [
    path('', shorten_url, name='shorten_url'),
    path('list/', url_list, name='url_list'),
    path('<str:short_code>/', redirect_to_original, name='redirect_to_original'),
]