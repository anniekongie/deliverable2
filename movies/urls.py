from django.urls import path
from . import views


urlpatterns = [
    path('<str:title>', views.viewMovie,name='viewMovie'),
    path('sort/<str:modelType>', views.movieSort, name='movieSort'),
    path('searchresult/', views.movieSearch, name='movieSearch'),
]
