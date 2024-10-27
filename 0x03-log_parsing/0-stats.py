#!/usr/bin/python3

import sys
import signal
import re

input_format = r'^(\S+) - \[(.+)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
# <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

total = 0
counter = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Define the signal handler for keyboard interruption (CTRL + C)
def handle_interrupt(signum, frame):
    print_metrics()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_interrupt)

# Function to print the metrics as specified
def print_metrics():
    print("File size: {}".format(total))
    for code in sorted(counter):
        if counter[code] > 0:
            print("{}: {}".format(code, counter[code]))

# Process each line from standard input
for line in sys.stdin:
    match = re.match(input_format, line)
    if match:
        status_code = int(match.group(3))
        file_size = int(match.group(4))
        
        # Update total file size and status code count if the status code is recognized
        total += file_size
        if status_code in counter:
            counter[status_code] += 1

        line_count += 1

        # Every 10 lines, print the metrics
        if line_count % 10 == 0:
            print_metrics()
    else:
        continue

print_metrics()
