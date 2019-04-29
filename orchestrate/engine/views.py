from django.shortcuts import render
import requests

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

from .models import Count
from .utils import increment_count, prev_con, container_list
class ProxyView(APIView):
	def get(self, request, id):
		increment_count()
		global prev_con
		ip = "http://127.0.0.1:"
		print(container_list)
		print(ip + str(list(container_list[((prev_con + 1) % len(container_list))].keys())[0]) + "/api/v1/" + id)
		prev_con += 1
		res=requests.get(ip + str(list(container_list[((prev_con + 1) % len(container_list))].keys())[0]) + "/api/v1/" + id)
		return Response(res.json(), res.status_code)
	def post(self, request, id):
		increment_count()
		global prev_con
		ip = "http://127.0.0.1:"
		prev_con += 1
		res = requests.post(ip + str(list(container_list[((prev_con + 1) % len(
			container_list))].keys())[0]) + "/api/v1/" + id, data=request.POST)
		return Response(res.json(), res.status_code)
	def delete(self, request, id):
		increment_count()
		ip = "http://127.0.0.1:"
		global prev_con
		prev_con += 1
		res = requests.delete(
			ip + str(list(container_list[((prev_con + 1) % len(container_list))].keys())[0]) + "/api/v1/" + id)
		return Response(res.json(), res.status_code)
