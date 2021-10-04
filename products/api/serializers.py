from rest_framework import serializers


class SearchSerializer(serializers.Serializer):
    search_input = serializers.CharField(max_length=200)