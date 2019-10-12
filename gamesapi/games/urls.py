from django.urls import path
from games import views

urlpatterns = [
    path('games/', views.games_list),
    path('games/<int:pk>/', views.game_detail),
]