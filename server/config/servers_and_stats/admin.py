# Файл servers_and_stats/admin.py

from django.contrib import admin
from .models import Server, ServerStatus, ServerStatus2

@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'name', 'description', 'server_is_active')

@admin.register(ServerStatus)
class ServerStatusAdmin(admin.ModelAdmin):
    list_display = ('host', 'sysname', 'date', 'network', 'disk', 'mem_total', 'mem_used', 'mem_percent',
                  'cpu_cores', 'cpu_physical_cores', 'cpu_freqency', 'load_average')

@admin.register(ServerStatus2)
class ServerStatus2Admin(admin.ModelAdmin):
    list_display = ('date', 'host_information', 'network', 'disk', 'memory', 'cpu', 'load_average')
