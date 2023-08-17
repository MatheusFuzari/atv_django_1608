from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status

class LocationApiView(APIView):
  def post(self,request):
    locationJson = request.data
    LocationSerialized = LocationSerializer(data=locationJson)
    LocationSerialized.is_valid(raise_exception=True)
    LocationSerialized.save()
    return Response(data=LocationSerialized.data, status=status.HTTP_201_CREATED)
  def get(self,request,id=''):
    if(id==''):
      location_found = Location.objects.all()
      locationSerialized = LocationSerializer(location_found, many=True)
      return Response(locationSerialized.data)
    try:
      location_found = Location.objects.get(id=id)
      locationSerialized = LocationSerializer(location_found, many=False)
      return Response(locationSerialized.data)
    except Location.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND, data="Location not found!")

class EpisodeApiView(APIView):
  def post(self,request):
    episodeJson = request.data
    episodeSerialized = EpisodeSerializer(data=episodeJson)
    episodeSerialized.is_valid(raise_exception=True)
    episodeSerialized.save()
    return Response(data=episodeSerialized.data,status=status.HTTP_201_CREATED)
  def get(self,request,id=''):
    if(id==''):
      episode_found = Episode.objects.all()
      episodeSerialized = EpisodeSerializer(episode_found, many=True)
      return Response(episodeSerialized.data)
    try:
      episode_found = Episode.objects.get(id=id)
      episodeSerialized = EpisodeSerializer(episode_found, many=False)
      return Response(episodeSerialized.data)
    except Episode.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND, data='Episode not found!')

class CharacterApiView(APIView):
  def post(self,request):
    characterJson = request.data
    characterSerialized = CharactersSerializer(data=characterJson)
    characterSerialized.is_valid(raise_exception=True)
    characterSerialized.save()
    return Response(data=characterSerialized.data, status=status.HTTP_201_CREATED)
  def get(self,request,id=''):
    if(id==''):
      character_found = Character.objects.all()
      characterSerialized = CharactersSerializer(character_found, many=True)
      return Response(characterSerialized.data)
    try:
      character_found = Character.objects.get(id=id)
      characterSerialized = CharactersSerializer(character_found, many=False)
      return Response(characterSerialized.data)
    except Character.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND, data='Character not found!')