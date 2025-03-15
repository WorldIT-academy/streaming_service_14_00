from django.contrib import admin
from django.urls import path
from .views import render_films, add_to_favourite, render_favourite_films

urlpatterns = [
    path("all/", render_films, name="all_films"),
    path('add-to-favourite/<int:film_pk>', add_to_favourite, name="add_to_favourite"),
    path('favourite-films/', render_favourite_films, name='favourite_films')
    # path('add-to-favourite/', name="")
]