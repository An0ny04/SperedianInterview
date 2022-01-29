from django.shortcuts import render
from django.http import  HttpResponse
from .models import Employee
from django.http import JsonResponse
from .serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from bson.objectid import ObjectId
# Create your views here.


class EmployeeView(APIView):
    def get(self, request,pk=None):
        if pk:
            Employee_data = Employee.objects.filter(_id=ObjectId(pk))
            serializer = EmployeeSerializer(Employee_data, many=True)
            return Response(serializer.data)
        else:
            Employee_data = Employee.objects.all()
            serializer = EmployeeSerializer(Employee_data, many=True)
            return Response(serializer.data)

    def post(self,request):
        serializer = EmployeeSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except:
            return Response({'message': 'Only Post Allowed'})
    
    def put(self,request,pk=None):
        Employee_data = Employee.objects.get(_id=ObjectId(pk))
        if Employee_data:
            serializer = EmployeeSerializer(Employee_data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                serializer = EmployeeSerializer(Employee_data)
                return Response(serializer.data)
            return Response(serializer.errors)
        else:
            return Response({'message': 'data not found'})
    
    def delete(self, request, pk=None):
        Employee_data = Employee.objects.get(_id=ObjectId(pk))
        if Employee_data:
            Employee_data.delete()
            return Response({'message': 'Delete Successfull'})
        else:
            return Response({'message': 'data not found'})

