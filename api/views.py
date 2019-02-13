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
        print(sth.is_valid())
        print(sth.validated_data)
        r = JSONRenderer()
        data = r.render(dict())
        return Response(data=data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def remove_act(request,act_id):
    if request.method=='DELETE':
        instance=Act.objects.get(actId=act_id)
        ret = instance.delete()
        if ret[0]!=0:
            return Response(data={}, status=status.HTTP_200_OK)
        else:
            return Response(data={}, status= status.HTTP_400_BAD_REQUEST)

    else:
        print("Hello5")
        return Response(data={}, status= status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def upload_an_act(request):
    if request.method== 'POST':
        try:
            print(request.data)
            if (isValidB64(request.data['imgB64']) == False):
                    return Response(data={}, status=status.HTTP_400_BAD_REQUEST)
            print("loll")
            u = User.objects.get(username= request.data['username'])
            c = Category.objects.get(category_name= request.data['categoryName'])
            print("lolo")
            act= Act(actId=int(request.data['actId']),username= u,category= c,caption= str(request.data['caption']),image=str(request.data['imgB64']))
            print(act)
            act.save()
            return Response(data={}, status= status.HTTP_201_CREATED)
        except:
            return Response(data={}, status= status.HTTP_400_BAD_REQUEST)
    else:
        return Response(data={}, status= status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['DELETE'])
def delete_user_view(request,username):
        print(username)
        print(request.method)
        ret = User.objects.filter(username=username).delete()
        # ret[0] is 0 means 0 objects have been deleted, that is when there are no users with that username
        if ret[0] == 0:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(data ={},status=status.HTTP_200_OK)


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
        # l = Act.objects.all().values('category').order_by('category').annotate(
        #     total=Count('category'))
        l = Category.objects.all()
        op = dict()
        if (len(l) == 0):
            return Response(data={}, status=status.HTTP_204_NO_CONTENT)
        for i in l:
            op[i.category_name] = Act.objects.filter(category=i).count()
        #     print(Act.objects.filter(category=i).count())
        print("op",op)
        return Response(data=op,status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_category_view(request, category_name):
    print(category_name)
    if request.method == 'DELETE':
        instance = Category.objects.get(category_name=category_name)
        ret = instance.delete()
        if ret[0] != 0:
            return Response(data={}, status=status.HTTP_200_OK)
        else:
            return Response(data={}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(data={}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def get_category_act_view(request, category_name):
    if len(request.GET)!=0:
        print("miriams code")
        return list_act_in_category(request,category_name)
    if request.method == 'GET':
        try:
            response = []
            # print("hahahahaha",len(request.GET)==0)
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



@api_view(['GET'])
def list_num_acts_category(request,category_name):
        if request.method =='GET':
                try:
                        a = Category.objects.get(category_name=str(category_name))
                except Category.DoesNotExist:
                        return Response(data={},status=status.HTTP_400_BAD_REQUEST)
                acts =  Act.objects.filter(category__category_name=str(category_name)).count()
                #a1 = {"count":[acts]}
                a1 = [acts]
                if(acts>0):
                        return Response(data=a1,status = status.HTTP_200_OK)
                elif(acts==0):
                        return Response(data={},status=status.HTTP_204_NO_CONTENT)
        else:
                return Response(data={},status = status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['POST'])
def upvote_act(request):
        if request.method == 'POST':
                try:
                        print(request.data[0])
                        acts = Act.objects.get(actId=(request.data[0]))
                        acts.upvote += 1
                        acts.save()
                except:
                        return Response(data={},status=status.HTTP_400_BAD_REQUEST)
                return Response(data=[],status = status.HTTP_200_OK)
        else:
                return Response(data={},status = status.HTTP_405_METHOD_NOT_ALLOWED)



# @api_view(['GET'])
def list_act_in_category(request,category_name):
            print("my fghghjghunction call")
            try:
                    a = Category.objects.get(category_name=str(category_name))
            except:
                    return Response(data={},status = status.HTTP_400_BAD_REQUEST)
            acts = Act.objects.filter(category__category_name=str(category_name)).order_by('actId').reverse()
            print("@@@",acts)
            acts2 = []
            if(len(acts)==0):
                    return Response(data={},status = status.HTTP_204_NO_CONTENT)
            start = int(request.GET.get('start'))
            end = int(request.GET.get('end'))
            # count = Act.objects.filter(category__category_name=category_name).count()
            count = len(acts)
            print(count, end)
            if end>count:
                print("adada")
                return Response(data={},status= status.HTTP_400_BAD_REQUEST)
            for i in range(start-1,end):
                acts2.append(GetCategoryActResponseSerializer(GetCategoryActResponse(
                    acts[i].id, acts[i].username, acts[i].timestamp, acts[i].caption, acts[i].upvote, acts[i].image)).data)
            json_res = JSONRenderer().render(acts2)
            print("jsonres",json_res)
            if(len(acts2)>100):
                    return Response(data={},status = status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)
            else:
                    #ac1 = serializers.serialize('json',acts2)
                    return Response(data=json_res,status = status.HTTP_200_OK)
