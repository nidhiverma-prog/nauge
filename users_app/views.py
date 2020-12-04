from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.response import Response
from .serializers import ModelSerializer,UpdateSerializer
from users_app.models import *
# Create your views here.
from rest_framework import status
from rest_framework.parsers import JSONParser
# from users_app import folder
@api_view(('GET',))
def users_data(request):
    if request.method == 'GET':
        context=users_list.objects.all()
        data= owes.objects.all() 
        # owes = request.GET.get('sachin','rahul' ,'deepak',None)
        # owed_by=request.GET.get('sachin','rohit',None)
        # user=users_list.objects.all().first()
        # data_1=owed_by.objects.filter(name=1)
        # data_2=owed_by.objects.values_list('rohit',flat=True).get(pk=1)
        # d=data_1.values_list('sachin',flat=True)[0]
        # d2=data_1.values_list('rohit',flat=True)[0]
        # total=d+d2
        # b=balance(balance=total)
        # b.save()
        users_serializer = ModelSerializer(context, many=True)
        return JsonResponse(users_serializer.data, safe=False)
        # return Response(status=204)


@api_view(('POST',))
def add_user(request):
    if request.method == 'POST':
        add_data = JSONParser().parse(request)
        user_serializer =   ModelSerializer(data=add_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(('POST',))
def update(request):
    if request.method == 'POST':
        lender = request.data.get('lender',None)
        borrower=request.data.get('borrower',None)
        amount=request.data.get('amount',None)
        
        serializer=UpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)