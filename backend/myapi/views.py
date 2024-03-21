from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_world(request):
  return Response({'message': 'Hello, there!'})

@api_view(['GET'])
def api_root(request):
  return Response({'message': 'API Root. Use the endpoints to interact with the API.'})
