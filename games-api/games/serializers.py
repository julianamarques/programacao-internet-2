from rest_framework import serializers
from games.models import Game
from datetime import datetime


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

    
    def validate_name(self, name):
        self.game = Game.objects.filter(name=name)

        if self.game is not None:
            raise serializers.ValidationError("Já existe um jogo cadastrado com esse nome")

        return name


    def validate_delete(self, game):
        if game.released_date < datetime.now():
            raise serializers.ValidationError("Jogos já lançados não poodem ser excluídos")
