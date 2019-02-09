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
from .models import Category
from .models import Act

from django.core import serializers
# Create your views here.
@api_view(['POST'])
def add_user_view(request):
    if request.method == 'POST':
        sth = AddUserSerializer(data=request.data)
        print(sth.is_valid())
        print(sth['username'].value)
        user = User(username= sth['username'].value, password=sth['password'].value)
        user.save()
        print(sth.is_valid())
        print(sth.validated_data)
        r = JSONRenderer()
        data = r.render(dict())
        return Response(data=data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def add_category_view(request):
        if request.method =='POST':
                sth = AddUserSerializer(data=request.data)
                print(sth.is_valid())
                print(sth['category_name'].value)
                category = Category(category_name= sth['category_name'].value)
                category.save()
                print(sth.is_valid())
                print(sth.validated_data)
                r = JSONRenderer()
                data = r.render(dict())
                return Response(data=data, status=status.HTTP_201_CREATED)



@api_view(['DELETE'])
def delete_category_view(request,category_name):
        if request.method =='DELETE':
                sth = AddUserSerializer(data=request.data)
                print(sth.is_valid())
                print(category_name)
                instance = Category.objects.get(category_name= category_name)
                instance.delete()
                r = JSONRenderer()
                data = r.render(dict())
                return Response(data=data, status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def get_category_act_view(request, category_name):
        if request.method =='GET':
                data = serializers.serialize("json", Act.objects.get(category=category_name))
                # acts = Act.objects.all(category=category_name)
                # r = JSONRenderer()
                # data = r.render(dict())
                return Response(data=data, status=status.HTTP_200_OK)





