from django.shortcuts import render
from django.http import HttpResponse

import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import status

from .serializers import AddUserSerializer
from .request import AddUserRequest

from .models import User
from .utils import is_sha1
# Create your views here.
@api_view(['POST'])
def add_user_view(request):
    if request.method == 'POST':
        sth = AddUserSerializer(data=request.data)
        print(sth.is_valid())
        # print(sth['username'].value)
        if (is_sha1(sth['password'].value)):
                pass
        else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        user = User(username= sth['username'].value)
        user.save()
        user, created = User.objects.get_or_create(username=sth['username'].value)
        user.set_password(sth['password'].value)
        user.save()
        # print(sth.is_valid())
        # print(sth.validated_data)
        # r = JSONRenderer()
        # data = r.render(dict())
        return Response(data={}, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def delete_user_view(request,username):
        print(username)
        print(request.method)
        ret = User.objects.filter(username=username).delete()
        # ret[0] is 0 means 0 objects have been deleted, that is when there are no users with that username
        if ret[0] == 0:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)