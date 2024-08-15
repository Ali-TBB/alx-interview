#!/usr/bin/env python3
import sys
import signal
import re

# Regular expression to match the input format
r = r'(\d{1,3}(?:\.\d{1,3}){3}) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" ' \
    r'(\d{3}) (\d+)'
log_pattern = re.compile(r)

# Initialize metrics
total_size = 0
status_codes_count = {200: 0, 301: 0, 400: 0, 401: 0,
                      403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_statistics():
    """Function to print the statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


def process_line(line):
    """Process a single line of input."""
    global total_size, line_count

    match = log_pattern.match(line)
    if match:
        status_code = int(match.group(3))
        file_size = int(match.group(4))

        total_size += file_size

        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_statistics()


def signal_handler(sig, frame):
    """Handle keyboard interruption (Ctrl + C)."""
    print_statistics()
    sys.exit(0)


# Attach the signal handler for Ctrl+C
signal.signal(signal.SIGINT, signal_handler)


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            process_line(line.strip())
    except KeyboardInterrupt:
        print_statistics()
        sys.exit(0)

    print_statistics()
