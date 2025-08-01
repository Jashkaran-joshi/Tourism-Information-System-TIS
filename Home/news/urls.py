from django.urls import path

from . import views

urlpatterns = [
    path("", views.news, name="news"),
    path("news/category/<str:category>/", views.news_by_category, name="news_by_category"),
]
