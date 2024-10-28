# System Health Monitoring Script

## Overview

This Python script monitors the health of a Linux system by checking key metrics such as CPU usage, memory usage, disk space, and the number of running processes. If any of these metrics exceed predefined thresholds, the script logs a warning message to a log file and prints it to the console.

## Features

- **CPU Usage Monitoring**: Alerts if CPU usage exceeds 80%.
- **Memory Usage Monitoring**: Alerts if memory usage exceeds 80%.
- **Disk Space Monitoring**: Alerts if disk space usage exceeds 80%.
- **Running Processes Monitoring**: Alerts if the number of running processes exceeds 100.

## Requirements

- Python 3.x
- `psutil` library

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/system-health-monitor.git
   cd system-health-monitor
