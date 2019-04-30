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
		# print(ip + str(list(container_list[((prev_con + 1) % len(container_list))].keys())[0]) + "/api/v1/" + id)
		# res=requests.get(ip + str(list(container_list[((prev_con + 1) % len(container_list))].keys())[0]) + "/api/v1/" + id)
		res = requests.get(ip+"8000"+"/api/v1/"+id)
		prev_con += 1
		# print(res)
		try:
			data = res.json()
		except:
			data = {}
		try:
			status = res.status_code
		except:
			status = 200
		return Response(data,status)
	def post(self, request, id):
		increment_count()
		global prev_con
		ip = "http://127.0.0.1:"
		# res = requests.post(ip + str(list(container_list[((prev_con + 1) % len(
			# container_list))].keys())[0]) + "/api/v1/" + id, data=request.POST)
		print(request.data)
		res = requests.post(ip + "8000" + "/api/v1/" + id, json=request.data)

		prev_con += 1
		try:
			data = res.json()
		except:
			data = {}
		try:
			status = res.status_code
		except:
			status = 200
		return Response(data, status)
	def delete(self, request, id):
		increment_count()
		ip = "http://127.0.0.1:"
		global prev_con
		res = requests.delete(
			ip + str(list(container_list[((prev_con + 1) % len(container_list))].keys())[0]) + "/api/v1/" + id)
		prev_con += 1
		try:
			data = res.json()
		except:
			data = {}
		try:
			status = res.status_code
		except:
			status = 200
		return Response(data, status)
