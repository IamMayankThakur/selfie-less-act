from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics

from .serializers import AddUserSerializer
from .request import AddUserRequest
# Create your views here.
@api_view(['GET', 'POST'])
def add_user_view(request):
    if request.method == 'POST':
        sth = AddUserSerializer(request)
        print(sth.username)
        # print(sth.data)
        return Response("hii")
