# Файл servers_and_stats/serializer.py

from rest_framework import serializers
from .models import Server, ServerStatus


class ServerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Server
        fields = ['id', 'ip_address', 'description', 'name', 'server_is_active']


class ServerShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Server
        fields = ['ip_address', 'server_is_active']


class ServerStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServerStatus
        fields = ['id', 'host', 'sysname', 'date', 'network', 'disk', 'mem_total', 'mem_used', 'mem_percent',
                  'cpu_cores', 'cpu_physical_cores', 'cpu_freqency', 'load_average']
