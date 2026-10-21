import psutil
import time
print("Real time system resources")
print("press ctrl+C to stop")
while True:
    cpu=psutil.cpu_percent(interval=1)
    ram=psutil.virtual_memory().percent
    disk=psutil.disk_usage("/").percent
    print("/n------------------------")
    print(f"Cpu usage:{cpu}%")
    print(f"Ram usage:{ram}%")
    print(f"Disk usage:{disk}%")
    if cpu > 80:
        print("Warning: Cpu usage is above 80%!")
    if ram > 80:
        print("Warning: Ram usage is above 80%!")
    time.sleep(3)