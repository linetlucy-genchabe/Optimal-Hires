from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *

# Create your views here.


def index(request):
   
    
    return render(request, 'index.html')

@csrf_exempt
def JobApi(request,id=0):
    if request.method=='GET':
        jobs = Job.objects.all()
        jobs_serializer = JobSerializer(jobs, many=True)
        return JsonResponse(jobs_serializer.data, safe=False)

    elif request.method=='POST':
        job_data=JSONParser().parse(request)
        jobs_serializer = JobSerializer(data=job_data)
        if jobs_serializer.is_valid():
            jobs_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        job_data = JSONParser().parse(request)
        job=Job.objects.get(jobid=job_data['jobId'])
        jobs_serializer=JobSerializer(job,data=job_data)
        if jobs_serializer.is_valid():
            jobs_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        job=Job.objects.get(jobId=id)
        job.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

    
class CategoryView(APIView):
     #APIView as a base class for our API view function.
    def get(self, request, format=None):
        #define a get method where we query the database to get all the MoringaMerchobjects
        all_types = Category.objects.all()
        #serialize the Django model objects and return the serialized data as a response.
        serializers = CategorySerializer(all_types, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        # post method will be triggered when we are getting form data
        serializers = CategorySerializer(data=request.data)
        # serialize the data in the request
        if serializers.is_valid():
            # If valid we save the new data to the database and return the appropriate status code.
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)




class JobtypeView(APIView):
     #APIView as a base class for our API view function.
    def get(self, request, format=None):
        #define a get method where we query the database to get all the MoringaMerchobjects
        all_types = Jobtype.objects.all()
        #serialize the Django model objects and return the serialized data as a response.
        serializers = JobtypeSerializer(all_types, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        # post method will be triggered when we are getting form data
        serializers = JobtypeSerializer(data=request.data)
        # serialize the data in the request
        if serializers.is_valid():
            # If valid we save the new data to the database and return the appropriate status code.
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)







    

