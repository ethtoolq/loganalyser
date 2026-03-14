# Log Analyzer

Log Analyzer — a simple Python script for analyzing log files.

The script reads a log file and shows a small set of statistics.

## Features

    count all lines
    count errors (error)
    count warnings (warning)
    find the most frequent IP addresses

## Requirements

    Python 3

No additional libraries required.

## Usage

```bash
python3 log_analyzer.py server.log
```

## Example output

```
log statistics
--------------
total lines : 120
errors      : 5
warnings    : 3

top ip addresses
----------------
192.168.1.1 - 34 requests
192.168.1.5 - 12 requests
192.168.1.8 - 7 requests
```
## Purpose

The project is made for practice:

    Python
    CLI programs
    working with files
    data analysis

## License
MIT
