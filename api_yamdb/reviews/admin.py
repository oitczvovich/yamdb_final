from django.contrib import admin

from .models import Category, Comment, Genre, GenreTitle, Review, Title, User

reviews_models = [Category, Comment, Genre, GenreTitle, Review, Title, User]
admin.site.register(reviews_models)
