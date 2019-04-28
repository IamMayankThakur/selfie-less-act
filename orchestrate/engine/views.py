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
from .apps import client, api_count, port


class ProxyView(APIView):
	def get(self, request, id):
		print(id)
		print(client.info())
		return Response(id)
	def post(self, request, id):
		pass
	def delete(self, request, id):
		pass
