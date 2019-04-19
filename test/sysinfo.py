import psutil

print("CPU load", psutil.cpu_percent(),'%')
print("RAM", psutil.virtual_memory())
print("Disk usage", psutil.disk_usage('.'))
