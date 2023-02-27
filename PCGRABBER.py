import psutil
import socket

ip_address = socket.gethostbyname(socket.gethostname())
cpu_count = psutil.cpu_count()
memory_info = psutil.virtual_memory()
disk_usage = psutil.disk_usage('/')
network_info = psutil.net_if_addrs()

with open(f'pcdata_{socket.gethostname()}.txt', 'w') as f:
    f.write(f"Hostname: {socket.gethostname()}\n")
    f.write(f"IP address: {ip_address}\n")
    f.write(f"CPU count: {cpu_count}\n")
    f.write(f"Total memory: {memory_info.total}\n")
    f.write(f"Available memory: {memory_info.available}\n")
    f.write(f"Used memory: {memory_info.used}\n")
    f.write(f"Percentage of memory usage: {memory_info.percent}%\n")
    f.write(f"Total disk space: {disk_usage.total}\n")
    f.write(f"Used disk space: {disk_usage.used}\n")
    f.write(f"Free disk space: {disk_usage.free}\n")
    f.write(f"Percentage of disk usage: {disk_usage.percent}%\n")
    for interface, addresses in network_info.items():
        f.write(f"Interface: {interface}\n")
        for address in addresses:
            if str(address.family) == 'AddressFamily.AF_INET':
                f.write(f"\tIP Address: {address.address}\n")
