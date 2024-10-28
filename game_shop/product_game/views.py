from rest_framework import generics
from .models import Game
from .pagination import OneItemPagination
from .serializers import GameSerializer


class GameListView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GamesByCategoryView(generics.ListAPIView):
    serializer_class = GameSerializer
    pagination_class = OneItemPagination

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        return Game.objects.filter(category__name=category_name)
