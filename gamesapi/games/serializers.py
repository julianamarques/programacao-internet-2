from rest_framework import serializers
from datetime import datetime

from .models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

    def validate_name(self, name):
        game = Game.objects.filter(name=name)

        if(game is not None):
            raise serializers.ValidationError('Já existe um jogo cadastrado com esse nome')

        return name

    def validade_delete(self, game):
        if game.released_data < datetime.now():
            raise serializers.ValidationError('Jogos já lançados não podem ser excluidos')
        
        return True
