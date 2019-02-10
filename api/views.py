from django.shortcuts import render
from django.http import HttpResponse
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

from .serializers import AddUserSerializer
from .serializers import AddCategorySerializer
from .serializers import GetCategoryActResponseSerializer
from .request import AddUserRequest
from .response import GetCategoryActResponse

from .models import User
from .utils import is_sha1
from .models import Category
from .models import Act

from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count

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


# Also the view for list all categories
@api_view(['POST', 'GET'])
def add_category_view(request):
        # print(request.data)
    if request.method == 'POST':
        for i in request.data:
            try:
                category = Category(category_name=i)
                category.save()
            except:
                return Response(data={}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={}, status=status.HTTP_201_CREATED)
    if request.method == 'GET':
        l = Act.objects.all().values('category').annotate(
            total=Count('category'))
        return Response(data=l,status=status.HTTP_200_OK)

        # method not allowed


@api_view(['DELETE'])
def delete_category_view(request, category_name):
    print(category_name)
    if request.method == 'DELETE':
        try:
            instance = Category.objects.get(category_name=category_name)
            instance.delete()
            return Response(data={}, status=status.HTTP_200_OK)
        except:
            return Response(data={}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(data={}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def get_category_act_view(request, category_name):
    if request.method == 'GET':
        try:
            response = []
            if(Act.objects.filter(category__category_name=category_name).exists()):
                act = Act.objects.filter(category__category_name=category_name)
                print(act)
                for i in act:
                    response.append(GetCategoryActResponseSerializer(GetCategoryActResponse(
                        i.id, i.username, i.timestamp, i.caption, i.upvote, i.image)).data)
                json_res = JSONRenderer().render(response)
                return Response(data=json_res, status=status.HTTP_200_OK)
            else:
                return Response(data={}, status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response(data={}, status=status.HTTP_204_NO_CONTENT)
