import requests
from os import environ
from sys import platform
import psutil
from socket import gethostname
from datetime import datetime
import json


def is_server_already_registered(api_url, hostname, ip, logger=None):
    '''
    Checks if server is already registered in database
    :param api_url: Full URL to API for the request. Ex.: http://127.0.0.1:8000/api/servers/
    :param hostname: Name of the host
    :param ip: IP-address of the host
    :param logger: Logging object (module logging)
    :return: True/False
    '''
    func_name = 'is_server_already_registered()'
    try:
        r = requests.get(api_url)
        for i in r.json():
            if i['ip_address'] == ip and i['name'] == hostname:
                return True
        return False
    except requests.exceptions.ConnectionError:
        msg = f'Function {func_name}. Cannot connect to {api_url}'
        if logger:
            logger.error(msg)
        else:
            print(msg)
        return False


def register_a_server(api_url, hostname, ip, server_is_active=False, description='', logger=None):
    '''
    :param api_url: Full URL to API for the request. Ex.: http://127.0.0.1:8000/api/servers/add
    :param hostname: Name of the host
    :param ip: IP-address of the host
    :param description: Some description for the host
    :param server_is_active: Is host an active? For client host you should set True
    :param logger: Logging object (module logging)
    :return: True/False
    '''
    func_name = 'register_a_server()'
    payload = {'ip_address': ip,
               'name': hostname,
               'description': description,
               'server_is_active': server_is_active}
    try:
        r = requests.post(api_url, data=payload)
        if r.status_code < 400:
            return True
        else:
            return False
    except requests.exceptions.ConnectionError as e:
        msg = f'Function {func_name}. Cannot connect to {api_url}'
        if logger:
            logger.error(msg)
        else:
            print(msg)
        return False


def get_hostname(logger=None):
    '''
    :param logger: Logging object (module logging)
    :return: Name of host that is gotten from an environment variable. Or '' in an unsuccessful case.
    '''
    func_name = 'get_hostname()'
    if platform == 'win32':
        host_env_name = 'COMPUTERNAME'
    else:
        host_env_name = 'HOSTNAME'
    try:
        hostname = environ[host_env_name]
        if logger:
            logger.debug(f"Function {func_name}. Hostname '{hostname}' is gotten " +
                         f"from environment variable: '{host_env_name}'")
        return hostname
    except KeyError as e:
        msg = f'No environment variable {host_env_name} for the platform {platform}'
        if logger:
            logger.warn(msg)
        else:
            print(msg)
        return ''


def get_system_info():
    '''
    :return: Dictionary with some system information
    '''
    net_interfaces = [{'interface': i[0], 'status': 'up' if i[1][0] else 'down', 'mtu': i[1][3]}
                      for i in psutil.net_if_stats().items()]
    disks = []
    for i in psutil.disk_partitions(True):
        du = psutil.disk_usage(i[1])
        disks.append({'disk': i[0], 'mountpoint': i[1], 'file_system_type': i[2], 'total': du[0], 'used': du[1]})
    mem = psutil.virtual_memory()
    cpu_freq = psutil.cpu_freq()
    la = psutil.getloadavg()

    sys_info_dict = {'host_information': {'sysname': platform, 'hostname': gethostname()},
        'network': net_interfaces,
        'disk': disks,
        'memory': {'memory_total': mem[0], 'memory_used': mem[3], 'memory_percent': mem[2]},
        'cpu': {'cpu_cores': psutil.cpu_count(), 'cpu_physical_cores': psutil.cpu_count(logical=False),
                'cpu_freqency': {'current': cpu_freq[0], 'min': cpu_freq[1], 'max': cpu_freq[2]}},
        'load_average': {'1 min': la[0], '5 min': la[1], '15 min': la[2]}
    }
    return sys_info_dict


def post_server_status(api_url, sys_info=None, logger=None):
    '''
    :param api_url: Full URL to API for the request. Ex.: http://127.0.0.1:8000/api/servers_status/add
    :param sys_info: System information - result of call get_system_info()
    :param logger: Logging object (module logging)
    :return: True/False
    '''
    func_name = 'post_server_status()'
    if not sys_info:
        sys_info = get_system_info()

    payload = {'host': sys_info['host_information']['hostname'],
               'sysname': sys_info['host_information']['sysname'],
               'date': datetime.now(),
               'network': json.dumps(sys_info['network']),
               'disk':  json.dumps(sys_info['disk']),
               'mem_total':  sys_info['memory']['memory_total'],
               'mem_used':  sys_info['memory']['memory_used'],
               'mem_percent': sys_info['memory']['memory_percent'],
               'cpu_cores': sys_info['cpu']['cpu_cores'],
               'cpu_physical_cores': sys_info['cpu']['cpu_physical_cores'],
               'cpu_freqency': json.dumps(sys_info['cpu']['cpu_freqency']),
               'load_average': json.dumps(sys_info['load_average'])}
    try:
        r = requests.post(api_url, data=payload)
        if r.status_code < 400:
            if logger:
                logger.info(f'Function {func_name}. The next info is successfully sent to {api_url}: {payload}')
            return True
        else:
            return False
    except requests.exceptions.ConnectionError:
        msg = f'Function {func_name}. Cannot connect to {api_url}'
        if logger:
            logger.error(msg)
        else:
            print(msg)
        return False


def post_server_status2(api_url, sys_info=None, logger=None):
    '''
    :param api_url: Full URL to API for the request. Ex.: http://127.0.0.1:8000/api/servers_status2/add
    :param sys_info: System information - result of call get_system_info()
    :param logger: Logging object (module logging)
    :return: True/False
    '''
    func_name = 'post_server_status2()'
    if not sys_info:
        sys_info = get_system_info()

    payload = {'date': datetime.now(),
               'host_information': json.dumps(sys_info['host_information']),
               'network': json.dumps(sys_info['network']),
               'disk': json.dumps(sys_info['disk']),
               'memory': json.dumps(sys_info['memory']),
               'cpu': json.dumps(sys_info['cpu']),
               'load_average': json.dumps(sys_info['load_average'])}
    try:
        r = requests.post(api_url, data=payload)
        if r.status_code < 400:
            if logger:
                logger.info(f'Function {func_name}. The next info is successfully sent to {api_url}: {payload}')
            return True
        else:
            return False
    except requests.exceptions.ConnectionError as e:
        msg = f'Function {func_name}. Cannot connect to {api_url}'
        if logger:
            logger.error(msg)
        else:
            print(msg)
        return False
