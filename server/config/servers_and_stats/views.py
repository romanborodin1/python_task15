from rest_framework import generics
from .serializer import ServerSerializer, ServerShortSerializer, ServerStatusSerializer, ServerStatus2Serializer
from .models import Server, ServerStatus, ServerStatus2

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


class ServerStatus2ViewSet(generics.ListAPIView):

    queryset = ServerStatus2.objects.all()
    serializer_class = ServerStatus2Serializer

class ServerStatus2AddView(generics.CreateAPIView):

    queryset = ServerStatus2.objects.all()
    serializer_class = ServerStatus2Serializer

class ServerStatus2DetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = ServerStatus2.objects.all()
    serializer_class = ServerStatus2Serializer
