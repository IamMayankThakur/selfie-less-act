from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.http import JsonResponse

import io
import base64

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import status
import base64

from .serializers import AddUserSerializer
# from .serializers import AddCategorySerializer
from .serializers import AddCategorySerializer
from .serializers import GetCategoryActResponseSerializer
from .request import AddUserRequest
from .response import GetCategoryActResponse

from .models import User
from .utils import is_sha1
from .utils import isValidB64

from rest_framework.views import APIView

from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count

# Create your views here.
class UserView(APIView):
        def post(self, request):
                sth = AddUserSerializer(data=request.data)
                print(sth.is_valid())
                if (is_sha1(sth['password'].value)):
                        pass
                else:
                        return Response(status=status.HTTP_400_BAD_REQUEST)
                user = User(username=sth['username'].value)
                user.save()
                print(sth.is_valid())
                print(sth.validated_data)
                r = JSONRenderer()
                data = r.render(dict())
                return Response(data=data, status=status.HTTP_201_CREATED)
        def get(self, request):
                users = User.objects.values_list('username', flat=True)
                print(users)
                return Response(data=users, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_user_view(request,username):
        print(username)
        print(request.method)
        ret = User.objects.filter(username=username).delete()
        # ret[0] is 0 means 0 objects have been deleted, that is when there are no users with that username
        if ret[0] == 0:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(data ={},status=status.HTTP_200_OK)
