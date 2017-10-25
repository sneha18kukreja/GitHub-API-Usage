from rest_framework import serializers
from .models import SearchUsers

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchUsers
        fields = '__all__'