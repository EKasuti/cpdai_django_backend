from rest_framework.decorators import serializers

class HelloWorldSerializer(serializers.Serializer):
    message = serializers.CharField()
