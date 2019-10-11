from django.conf.urls import url
from django.urls import path
from games import views

urlpatterns = [
    path('games/', views.games_list),
    path('games/<int:id>', views.game_detail)
]