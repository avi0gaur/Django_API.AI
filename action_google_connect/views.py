from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Chat_Response
from .serializers import Chat_ResponseSerializer
from rest_framework.decorators import api_view


# # send response based on HTTP request
# class ChatBot_Response(APIView):
#
#     # def get(self, request):
#     #     chat_res = Chat_Response.objects.all()
#     #     serializer = Chat_ResponseSerializer(chat_res, many=True)
#     #     return Response(serializer.data)
#
#     parser_classes = (JSONParser,)


@api_view(['GET', 'POST'])
def chatbot_response(request):
    if request.method == 'POST':
        chat_res = Chat_Response.objects.all()
        serializer = Chat_ResponseSerializer(chat_res, many=True)
        return Response(serializer.data)
