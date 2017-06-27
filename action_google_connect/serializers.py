from rest_framework import serializers

from .models import Chat_Response

class Chat_ResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat_Response
        fields = '__all__'
