from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

from rest_framework.parsers import MultiPartParser, FormParser


from home.serilizers import *
# Create your views here.

class handlefileupload(APIView):
	parser_classes = [MultiPartParser]
	def post(self, request, format=None):
		try:
			serializer = FileListSerilizers(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			else:
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response(str(e), status=status.HTTP_400_BAD_REQUEST)