#pip install psutil
import psutil

# CPU
# uncomment below to get only the physical cores
# print(psutil.cpu_count(logical=False))
print(psutil.cpu_count())
print(psutil.cpu_percent(interval=1)) # interval of 1 second
print(psutil.cpu_times())
print(psutil.cpu_stats())
print(psutil.cpu_freq())

# RAM
print(psutil.virtual_memory())
print(psutil.swap_memory())

# Hard Disk / Storage
print(psutil.disk_usage('C:\\'))
# uncomment below for Unix system
# print(psutil.disk_usage('/'))
print(psutil.disk_partitions())