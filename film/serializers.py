from rest_framework import serializers
from .models import Film, Gambar

class GambarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gambar
        fields = "__all__"

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = "__all__"

    def create(self, validated_data):

        try:
            # Here is the important part! Creating new object!
            instance = Film.objects.create(**validated_data)
        except TypeError:
            raise TypeError(msg)


    def save(self, **kwargs):

        validated_data = dict(
            list(self.validated_data.items()) +
            list(kwargs.items())
        )

        if self.instance is not None:
            self.instance = self.update(self.instance, validated_data)
        return self.instance
