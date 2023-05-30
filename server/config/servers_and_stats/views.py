from rest_framework import generics
from .serializer import ServerSerializer, ServerShortSerializer, ServerStatusSerializer
from .models import Server, ServerStatus

class ServerViewSet(generics.ListAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class ServerAddView(generics.CreateAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class ServerDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class ServerShortViewSet(generics.ListAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerShortSerializer

class ServerShortAddView(generics.CreateAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerShortSerializer

class ServerShortDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerShortSerializer


class ServerStatusViewSet(generics.ListAPIView):

    queryset = ServerStatus.objects.all()
    serializer_class = ServerStatusSerializer

class ServerStatusAddView(generics.CreateAPIView):

    queryset = ServerStatus.objects.all()
    serializer_class = ServerStatusSerializer

class ServerStatusDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = ServerStatus.objects.all()
    serializer_class = ServerStatusSerializer