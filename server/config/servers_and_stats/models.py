from django.db import models


class Server(models.Model):

    name = models.CharField('name', max_length=255)
    ip_address = models.GenericIPAddressField('IP', max_length=16, default='0.0.0.0')
    description = models.TextField('description', max_length=255, default='no_description')
    server_is_active = models.BooleanField('is_active', default=False)

    class Meta:
        managed = True
        verbose_name = 'Server'


class ServerStatus(models.Model):

    host = models.CharField('hostname', max_length=255)
    sysname = models.CharField('sysname', max_length=255)
    date = models.DateTimeField('datetime', auto_now_add=True)
    network = models.JSONField('net', max_length=10000)
    disk = models.JSONField('disk', max_length=10000)
    mem_total = models.PositiveBigIntegerField('mem_total')
    mem_used = models.PositiveBigIntegerField('mem_used')
    mem_percent = models.FloatField('mem_percnt')
    cpu_cores = models.PositiveSmallIntegerField('cpu_cores')
    cpu_physical_cores = models.PositiveSmallIntegerField('cpu_phys_cores')
    cpu_freqency = models.JSONField(max_length=100)
    load_average = models.JSONField(max_length=100)

    class Meta:
        managed = True
        verbose_name = 'ServerStatus'


class ServerStatus2(models.Model):

    date = models.DateTimeField('datetime', auto_now_add=True)
    host_information = models.JSONField('host_info', max_length=255)
    network = models.JSONField('net', max_length=5000)
    disk = models.JSONField('disk', max_length=5000)
    memory = models.JSONField('memory', max_length=150)
    cpu = models.JSONField('cpu', max_length=5000)
    load_average = models.JSONField('load_avrg', max_length=100)

    class Meta:
        managed = True
        verbose_name = 'ServerStatus2'
