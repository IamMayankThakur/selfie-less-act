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
import base64

from .serializers import AddUserSerializer
<<<<<<< HEAD
#from .serializers import AddCategorySerializer
=======
# from .serializers import AddCategorySerializer
>>>>>>> 08e9160e5310fc915eee18253dc4dbcbc9763fe8
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
		print("Hello2")
		try:
			print("Hello3")
			instance=Act.object.get(pk=act_id)
			instance.delete()
			return Response(data={}, status=status.HTTP_200_OK)
		except:
			print('Hello4')
			return Response(data={}, status= status.HTTP_400_BAD_REQUEST)

	else:
<<<<<<< HEAD
		print("Hello5")
		return Response(data={}, status= status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def upload_an_act(request):
	#print("Hello")
	if request.method== 'POST':
		#					print(type(request.data))
		try:
			act= Act()
			act.upvote=0
			#print("Hello2")

			act.username= request.data['username']
			#print("Hello3")
			act.category= str(request.data['categoryName'])
			act.caption= str(request.data['caption'])
			act.image= request.data['image']
			act.timestamp= request.data['timestamp']
			#act= Act(username, image, upvote, timestamp, caption, category)
			act.save()
			#print("Hello2")
			print(act.caption)
			return Response(data={}, status= status.HTTP_201_CREATED)
		except:
			return Response(data={}, status= status.HTTP_400_BAD_REQUEST)
	else:
		return Response(data={}, status= status.HTTP_405_METHOD_NOT_ALLOWED)








	

		

			








=======
		return Response(data={}, status= status.HTTP_405_METHOD_NOT_ALLOWED)
>>>>>>> 08e9160e5310fc915eee18253dc4dbcbc9763fe8
