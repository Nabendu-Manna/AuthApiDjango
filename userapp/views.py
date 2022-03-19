from urllib import response
from django.shortcuts import render, redirect

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.serializers import Serializer
from rest_framework import status

from .models import *
from .serializers import *
from .forms import *

from django.contrib import messages
from rest_framework.authtoken.models import Token

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/tasks/',
        'Details': '/task/<str:pk>/',
        'Create': '/task/create/',
        'Creates': '/tasks/create/',
    }

    return Response(api_urls)


class StudentViews(APIView):
    
    def get(self, request, *args, **kwargs):
        user =  Student.objects.all()
        serializer = StudentSerializers(user, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    

    def post(self, request, *args, **kwargs):
        form = signupForm(request.data)
        print('POST')
        if form.is_valid():
            print('valid')
            form.save()
            
            name = request.data['username']
            
            u = User.objects.filter(username = name)
            userId = u[0]
            customer = Student(user = userId, name = name)
            customer.save()

            userPassword = request.data['password1']

            responseData = {
                'status': 'ok',
                'user_name': name,
                'password': userPassword,
            }

        else:
            responseData = {
                'status': 'not_ok',
                'messages': 'username, email, first_name, last_name, password1, password2'
            }

        return Response(responseData)

@api_view(['post'])
def details(request):
    if "token" in request.data.keys():
        userToken = request.data['token']
        user = Token.objects.get(key = userToken).user.student

        serializer = StudentSerializers(user)
        return Response(serializer.data, status = status.HTTP_200_OK)

        # return Response(request.headers['Authtoken'], status = status.HTTP_201_CREATED)
    else:
        return Response({'message': "token not found!"}, status = status.HTTP_400_BAD_REQUEST)
