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
# from .serializers import AddCategorySerializer
from .request import AddUserRequest

from .models import User
from .models import Act
from .models import Category

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


@api_view(['DELETE'])
def remove_act(request,act_id):
	if request.method=='DELETE':
		try:
			instance=Act.object.get(pk=act_id)
			instance.delete()
			return Response(data={}, status=status.HTTP_200_OK)
		except:
			return Response(data={}, status= status.HTTP_400_BAD_REQUEST)

	else:
		return Response(data={}, status= status.HTTP_405_METHOD_NOT_ALLOWED)