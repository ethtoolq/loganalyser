import argparse
from collections import Counter
import re


def analyze_log(file_path):
    total = 0
    errors = 0
    warnings = 0
    ips = []

    ip_pattern = r"\b\d{1,3}(?:\.\d{1,3}){3}\b"

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            total += 1

            line_lower = line.lower()

            if "error" in line_lower:
                errors += 1

            if "warning" in line_lower:
                warnings += 1

            found_ips = re.findall(ip_pattern, line)
            ips.extend(found_ips)

    top_ips = Counter(ips).most_common(5)

    print("\nlog statistics")
    print("--------------")
    print(f"total lines : {total}")
    print(f"errors      : {errors}")
    print(f"warnings    : {warnings}")

    print("\ntop ip addresses")
    print("----------------")

    for ip, count in top_ips:
        print(f"{ip} - {count} requests")


def main():
    parser = argparse.ArgumentParser(description="simple log analyzer")
    parser.add_argument("file", help="log file")

    args = parser.parse_args()

    analyze_log(args.file)


if __name__ == "__main__":
    main()