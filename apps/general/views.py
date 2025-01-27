from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from .models import University
from .serializers import UniversitySerializer
from rest_framework.response import Response



class UniversityAPIView(APIView):
    def get(self, request):
        university = University.objects.all()
        serializer = UniversitySerializer(university, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UniversitySerializer(data=request.data)


