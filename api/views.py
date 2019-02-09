from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import status

from .serializers import AddUserSerializer
from .serializers import AddCategorySerializer
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
                try:
                        # sth = AddCategorySerializer(data=request.data)
                        # print(sth.is_valid())
                        # print(sth['category_name'].value)
                        category = Category(category_name= request['category_name'].value)
                        category.save()
                        # print(sth.is_valid())
                        # print(sth.validated_data)
                        # r = JSONRenderer()
                        # data = r.render(dict())
                        return Response(data={}, status=status.HTTP_201_CREATED)
                except:
                        r = JSONRenderer()
                        data = r.render(dict())
                        return Response(data=data, status = status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
                # r = JSONRenderer()
                # data = r.render(dict())
                return Response(data=data, status= status.HTTP_400_BAD_REQUEST)
                
                #method not allowed


@api_view(['DELETE'])
def delete_category_view(request,category_name):
        if request.method =='DELETE':
                try:
                        instance = Category.objects.get(category_name= category_name)
                        instance.delete()
                        return Response(data={}, status=status.HTTP_200_OK)
                except:
                        return Response(data={},status=status.HTTP_400_BAD_REQUEST)
        else:
                return Response(data={},status= status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def get_category_act_view(request, category_name):
        # print(category_name)
        # data = Act.objects.filter(category__category_name=str(category_name))
        # print(data)
        if request.method =='GET':

                try:
                        # acts= Act.objects.filter(category__category_name=category_name)
                        # print(acts)
                        acts = serializers.serialize("json", Act.objects.filter(category__category_name=category_name))
                        print(acts)
                        # print(acts.count())
                #         if(acts.count()>500):
                #                 return Response(data={},status=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)
                # # acts = Act.objects.all(category=category_name)
                #         print(acts)
                        return Response(data=acts)
                except:
                        return Response(data={},status=status.HTTP_204_NO_CONTENT)

                
        else:
                return Response(data={},status = status.HTTP_405_METHOD_NOT_ALLOWED)





