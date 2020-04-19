from rest_framework import serializers

class HelloApiSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=10)