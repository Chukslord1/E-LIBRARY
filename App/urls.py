import os
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls.static import static
from . import views
app_name = "APP"
urlpatterns = [
    path("", views.login, name="login"),
    path("index.html", views.index, name="index"),
    path("book_list", views.book_list, name="book-list"),
    path("book-list.html", views.book_list, name="book-list"),
    path("book_allotment", views.book_allotment, name="book-allotment"),
    path("book-allotment.html", views.book_allotment, name="book-allotment"),
    path("book_series", views.book_series, name="book-series"),
    path("series.html", views.book_series, name="book-series"),
    path("book_genre", views.book_genre, name="book-series"),
    path("genre.html", views.book_genre, name="book-series"),
    path("book_lang", views.book_lang, name="book-lang"),
    path("language.html", views.book_lang, name="book-lang"),
    path("members", views.members, name="members"),
    path("members.html", views.members, name="members"),
    path("login", views.login, name="login"),
    path("login.html", views.login, name="login"),
    path("roles", views.roles, name="roles"),
    path("roles.html", views.roles, name="roles"),
    path("author", views.author, name="author"),
    path("authors.html", views.author, name="author"),
    path("publisher", views.publisher, name="publisher"),
    path("publishers.html", views.publisher, name="publisher"),
    path("settings", views.e_settings, name="settings"),
    path("settings.html", views.e_settings, name="settings"),
    path("contact", views.contact, name="contact"),
    path("logout.html", views.logout, name="logout"),
]
