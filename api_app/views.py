from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


@api_view(['GET', 'POST'])
def index(request):
    print(request.auth, request.user)

    if request.method == 'GET':

        message = 'this is from get'
    elif request.method == 'POST':
        message = request.data
    else:
        message = 'not allowd'
    return Response(data=message, status=status.HTTP_200_OK)


class Message(APIView):
    def get(self, request):
        return Response(data='this is from class based view by get', status=status.HTTP_200_OK)

    def post(self, request):
        print(request.data)
        return Response(data="this is from class based view by post ", status=status.HTTP_200_OK)

