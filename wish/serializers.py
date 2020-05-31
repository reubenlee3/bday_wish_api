from rest_framework import serializers
from .models import Wish


class WishSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Wish
        fields = ['id', 'title', 'author', 'wish', 'image']
