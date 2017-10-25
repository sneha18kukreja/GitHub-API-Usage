from rest_framework import serializers
from .models import SearchUsers

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        login = SearchUsers
        fields = ('login', 'url')