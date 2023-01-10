#!/usr/bin/python3
import sys
from collections import defaultdict

# initialize variables to store metrics
total_size = 0
status_codes = defaultdict(int)

# read lines from stdin
line_count = 0
for line in sys.stdin:
    line_count += 1
    # split line by space
    parts = line.strip().split(" ")
    # extract file size and status code
    size = int(parts[-1])
    status = int(parts[-2])
    # update metrics
    total_size += size
    status_codes[status] += 1
    # print metrics every 10 lines or on keyboard interruption
    if line_count % 10 == 0:
        print_metrics(total_size, status_codes)

# print final metrics
print_metrics(total_size, status_codes)

def print_metrics(total_size, status_codes):
    # print total size
    print("Total file size:", total_size)
    # print number of lines by status code
    for status in sorted(status_codes):
        if status in [200, 301, 400, 401, 403, 404, 405, 500]:
            print("{}: {}".format(status, status_codes[status]))
