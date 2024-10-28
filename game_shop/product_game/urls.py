from django.urls import path
from .views import GameListView, GamesByCategoryView

urlpatterns = [
    path('games/', GameListView.as_view(), name='game-list'),
    path('games/category/<str:category_name>/', GamesByCategoryView.as_view(), name='games-by-category'),
]