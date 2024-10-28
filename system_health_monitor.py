import psutil
import logging
import time

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define thresholds
CPU_THRESHOLD = 80  # percent
MEMORY_THRESHOLD = 80  # percent
DISK_THRESHOLD = 80  # percent

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'High CPU Usage: {cpu_usage}%')
        print(f'High CPU Usage: {cpu_usage}%')

def check_memory_usage():
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f'High Memory Usage: {memory_usage}%')
        print(f'High Memory Usage: {memory_usage}%')

def check_disk_space():
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f'High Disk Usage: {disk_usage}%')
        print(f'High Disk Usage: {disk_usage}%')

def check_running_processes():
    processes = psutil.pids()
    if len(processes) > 100:  # Example threshold for number of processes
        logging.warning(f'High Number of Running Processes: {len(processes)}')
        print(f'High Number of Running Processes: {len(processes)}')

def monitor_system():
    while True:
        check_cpu_usage()
        check_memory_usage()
        check_disk_space()
        check_running_processes()
        time.sleep(60)  # Check every 60 seconds

if __name__ == '__main__':
    print("Starting system health monitoring...")
    monitor_system()
