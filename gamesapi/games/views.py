from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
#from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Game
from .serializers import GameSerializer


@api_view(['GET', 'POST'])
def games_list(request):
    if request.method == 'GET':
        games = Game.objects.all()
        game_serializer = GameSerializer(games)

        return Response(game_serializer.data)

    elif request.method == 'POST':
        game_serializer = GameSerializer(data=request.data)

        if game_serializer.is_valid():
            game_serializer.save()

            return Response(status=status.HTTP_201_CREATED)
        
        return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def game_detail(request, id):
    try:
        game = Game.objects.get(id=id)
        
        if request.method == 'GET':
            game_serializer = GameSerializer(game)
            
            return Response(game_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            game_serializer = GameSerializer(game, data=request.data)
        
            if game_serializer.is_valid():
                game_serializer.save()
            
                return Response(status=status.HTTP_200_OK)
        
            return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        elif request.method == 'DELETE':
            game.delete()
        
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
