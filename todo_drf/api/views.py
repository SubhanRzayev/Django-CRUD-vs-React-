from typing import Generic
from django.http.response import Http404
from django.views import generic
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from todo_drf.api.serializers import TaskSerializers
from todo_drf.models import Task
from rest_framework import status



class ApiOverView(APIView):
    """
    All api url overview
    """
    def get(self,request, format=None):
        api_urls = {
            'list':'tasks/',
            'Detail View':'tasks/<int:pk>'
        }
        return Response(api_urls)


class TaskListApiView(generics.ListAPIView):
    """
    List all tasks, or create an new task
    """
    def get(self,request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializers(tasks,many=True)
        return Response(serializer.data)
    
    def post(self,request, format=None):
        serializers = TaskSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class TaskDetailApiView(APIView):
    """
    Retrieve, update or delete a task instance
    """
    
    
    def get_object(self,pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404
        
    def get(self,request,pk, format=None):
        task = self.get_object(pk)
        serializers = TaskSerializers(task)
        return Response(serializers.data)
    
    def post(self,request,pk, format=None):
        task = self.get_object(pk)
        serializers = TaskSerializers(task, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

    
    
        
    
    

        
    
    
