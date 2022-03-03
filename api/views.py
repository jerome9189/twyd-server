from django.shortcuts import render
from .forms import UpdatePreferencesForm, UpdateStatusForm
from rest_framework import viewsets, status

from .serializers import UserPreferencesSerializer, UserSerializer, UserStatusSerializer
from .models import Preferences, User, Status
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('user_name')
    serializer_class = UserSerializer


class RoomStatusViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Status.objects.all()
        serializer = UserStatusSerializer(queryset, many=True)
        return Response(serializer.data)


class StatusViewSet(viewsets.ViewSet):
    def update(self, request, pk=None):
        if not pk:
            return Response('No user specified', status.HTTP_400_BAD_REQUEST)
        try:
            instance = Status.objects.filter(pk=pk).get()
        except Exception as err:
            print(err)
            return Response(f'Could not update status for "{pk}"', status.HTTP_400_BAD_REQUEST)
        form = UpdateStatusForm(request.data, instance=instance)
        if form.is_valid():
            form.save()
            return Response('OK', status.HTTP_200_OK)
        return Response('Invalid data', status.HTTP_400_BAD_REQUEST)


class PreferencesViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        if not pk:
            return Response('No user specified', status.HTTP_400_BAD_REQUEST)
        try:
            instance = Preferences.objects.filter(pk=pk).get()
        except Exception as err:
            print(err)
            return Response(f'Could not get preferences for "{pk}"', status.HTTP_400_BAD_REQUEST)
        serializer = UserPreferencesSerializer(instance)
        return Response(serializer.data)
        
    def update(self, request, pk=None):
        print("hello")
        if not pk:
            return Response('No user specified', status.HTTP_400_BAD_REQUEST)
        try:
            instance = Preferences.objects.filter(pk=pk).get()
        except Exception as err:
            print(err)
            return Response(f'Could not update preferences for "{pk}"', status.HTTP_400_BAD_REQUEST)
        form = UpdatePreferencesForm(request.data, instance=instance)
        if form.is_valid():
            form.save()
            return Response('OK', status.HTTP_200_OK)
        return Response('Invalid data', status.HTTP_400_BAD_REQUEST)
