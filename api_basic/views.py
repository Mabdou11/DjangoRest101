from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Alien, Box
from .serializers import AlienSerializer, BoxSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['GET', 'POST'])
def alienList(request):

    if request.method == 'GET':
        aliens = Alien.objects.all()
        serializer = AlienSerializer(aliens, many=True)
        return JsonResponse(serializer.data, safe= False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serialiser = AlienSerializer(data=data)

        if serialiser.is_valid():
            serialiser.save()
            return JsonResponse(serialiser.data, status=201)
        return JsonResponse(serialiser.errors, status= 400)


@api_view(['GET', 'POST'])
def boxList(request):

    if request.method == 'GET':
        boxes = Box.objects.all()
        serializer = BoxSerializer(boxes, many=True)
        return JsonResponse(serializer.data, safe= False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serialiser = BoxSerializer(data=data)

        if serialiser.is_valid():
            serialiser.save()
            return JsonResponse(serialiser.data, status=201)
        return JsonResponse(serialiser.errors, status= 400)

@api_view(['GET', 'PUT', 'DELETE'])
def boxOne(request, pk):
    try:
        box = Box.objects.get(pk=pk)
    except Box.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = BoxSerializer(box)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serialiser = BoxSerializer(box, data=data)
        if serialiser.is_valid():
            serializer.save()
            return JsonResponse(serialiser.data)
    elif request.method == 'DELETE':
        box.delete()
        return HttpResponse(status=204)

@api_view(['GET', 'PUT', 'DELETE'])
def alienOne(request, pk):
    try:
        alien = Alien.objects.get(pk=pk)
    except Alien.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = AlienSerializer(alien)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serialiser = AlienSerializer(alien, data=data)
        if serialiser.is_valid():
            serializer.save()
            return JsonResponse(serialiser.data)
    elif request.method == 'DELETE':
        alien.delete()
        return HttpResponse(status=204)