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

    # {'host_information': {'sysname': 'win32', 'hostname': '5CD9512815'},
    # 'network': [
    #     {'interface': 'Ethernet', 'status': 'down', 'mtu': 1500},
    #     {'interface': 'VMware Network Adapter VMnet1', 'status': 'up', 'mtu': 1500},
    #     {'interface': 'VMware Network Adapter VMnet8', 'status': 'up', 'mtu': 1500},
    #     {'interface': 'Loopback Pseudo-Interface 1', 'status': 'up', 'mtu': 1500},
    #     {'interface': 'Беспроводная сеть', 'status': 'up', 'mtu': 1500},
    #     {'interface': 'Подключение по локальной сети* 1', 'status': 'down', 'mtu': 1500},
    #     {'interface': 'Подключение по локальной сети* 2', 'status': 'down', 'mtu': 1500}],
    # 'disk': [{'disk': 'C:\\', 'mountpoint': 'C:\\', 'file_system_type': 'NTFS', 'total': 249401421824, 'used': 178183073792}],
    # 'memory': {'memory_total': 8219471872, 'memory_used': 6440419328, 'memory_percent': 78.4},
    # 'cpu': {'cpu_cores': 8, 'cpu_physical_cores': 4, 'cpu_freqency': {'current': 1600.0, 'min': 0.0, 'max': 1800.0}},
    # 'load_average': {'1 min': 0.0, '5 min': 0.0, '15 min': 0.0}}

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
