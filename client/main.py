'''
Используя полученные знания, напишите клиентскую часть нашего приложения.

Идея клиента следующая: сбор и отправка данных о системе на сервер, который мы сделали на предыдущем уроке.
Это свободное задание, в котором вам нужно проявить фантазию. Тем не менее, программа должна обеспечивать
следующие функции:

1. При запуске программы, она должна регистрировать наш клиент на сервере (`POST`запрос на`api/servers/add`)
    - Для определения внешнего IP адреса используйте`requests.get('https://ifconfig.me/ip').text`, либо используйте
    любой другой доступный способ определения IP.
    - В поле `name` подавать значение `hostname`
    - В поле `description` брать значение из переменной окружения

2. Программа должна обрабатывать данные о системе, полученные от утилиты `psutil`, и отправлять их на сервер с
интервалом в 1 минуту в формате:
    {'host_information': {'sysname': ..., 'hostname' : ...},
     'network': [{'interface': up/down, 'mtu': ... }...],
     'disk': [{'disk: ..., 'mountpoint': ..., 'file_system_type', 'total': ..., 'used': ....} ],
     'memory': {'memory_total': ..., 'memory_used': ..., 'memory_percent': ...},
     'cpu': {'cpu_cores': ..., 'cpu_physical_cores': ..., 'cpu_freqency': {...}},
     'load_average': {'1 min': ..., '5 min': ..., '15 min': ...}}}
Это не окончательный список данных. Вы можете добавить те данные, которые посчитаете нужными. И даже что-то убрать.

3. Программа должна логировать следующие этапы работы:
    - INFO - Старт программы,
    - INFO - Успешная регистрация сервера,
    - INFO - Полученный в результате работы массив данных о системе,
    - ERROR - При отказе отправки данных или регистрации сервера.

Вы также можете дописать нашу серверную часть и добавить модель и соответствующее представление для приема данных.
Но это не обязательно.

Обрабатывайте исключения, которые вызывают запросы. В этом вам помогут исключения из requests.exceptions.

Можете организовать проверку наличия данного сервера в регистрируемых серверах, чтобы не делать повторную регистрацию.

Также вы можете добавить логирование тех моментов, которые посчитаете нужными.
'''
import requests
import socket
import logging
import schedule
import client_lib as cl

PERIOD = 60    # sec

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s [%(levelname)s] %(message)s',
                        datefmt='%d-%m-%Y %H:%M:%S')
    logging.info('The program is started')
    # Current variables:
    base_url = 'http://127.0.0.1:8000/api'
    url_for_add_srv = f'{base_url}/servers/add'
    url_for_list_srv = f'{base_url}/servers/'
    url_for_add_info = f'{base_url}/servers_status/add'
    url_for_add_info2 = f'{base_url}/servers_status2/add'
    ext_ip_url = 'https://ifconfig.me/ip'

    try:
        my_ip = requests.get(ext_ip_url).text
    except requests.exceptions.RequestException:
        my_ip = '127.0.0.1'
        logging.warning(f'Cannot get an external IP from {ext_ip_url}. Use the default value: {my_ip}')

    descr = f'Host: {cl.get_hostname(logging)}'
    hostname = socket.gethostname()
    if cl.is_server_already_registered(url_for_list_srv, hostname, my_ip, logging):
        logging.warning(f'Server [hostname: {hostname}, IP-address: {my_ip}] is already registered. '
                        f'Pass the registration of the server')
    else:
        is_registered = cl.register_a_server(url_for_add_srv, hostname, my_ip, True, descr, logging)
        if is_registered:
            logging.info(f'Server [hostname: {hostname}, IP-address: {my_ip}, is_active: True] ' +
                         f'is successfully registered')
        else:
            logging.error(f'Server [hostname: {hostname}, IP-address: {my_ip}, is_active: True] ' +
                          f'is not registered')

    def write_sys_info():
        sys_info = cl.get_system_info()
        logging.info(sys_info)
        # Fisrt way
        if cl.post_server_status(url_for_add_info, sys_info, logging):
            logging.info(f'[1] Info about server is added')
        else:
            logging.error(f'[1] Info about server is not added')
        # Second way
        if cl.post_server_status2(url_for_add_info2, sys_info, logging):
            logging.info(f'[2] Info about server is added')
        else:
            logging.error(f'[2] Info about server is not added')

    schedule.every(PERIOD).seconds.do(write_sys_info)
    while True:
        schedule.run_pending()
