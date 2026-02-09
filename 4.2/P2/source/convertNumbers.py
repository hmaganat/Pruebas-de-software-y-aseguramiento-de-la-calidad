#!/usr/bin/env python3
"""
convertNumbers.py

Converts numbers from a file to binary and hexadecimal.
Handles negative numbers.
"""

import sys
import time


def read_numbers(file_path):
    """Read numbers from a file, handling invalid data."""
    numbers = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            value = line.strip()
            if not value:
                continue
            try:
                numbers.append(int(value))
            except ValueError:
                print(f"Invalid data at line {line_number}: '{value}'")
    return numbers


def to_binary(n):
    """Convert integer to binary string, show negative sign if needed."""
    if n == 0:
        return "0"
    negative = n < 0
    num = abs(n)
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
    return ("-" if negative else "") + binary


def to_hexadecimal(n):
    """Convert integer to hexadecimal string, 32-bit two's complement for negatives."""
    if n == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    if n < 0:
        n = (1 << 32) + n
    hex_str = ""
    num = n
    while num > 0:
        hex_str = hex_chars[num % 16] + hex_str
        num //= 16
    return hex_str


def main():
    """Main program."""
    if len(sys.argv) < 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    start_time = time.time()
    file_path = sys.argv[1]

    numbers = read_numbers(file_path)

    if not numbers:
        print("No valid numeric data found.")
        sys.exit(1)

    results = []
    for n in numbers:
        results.append(f"{n} -> binary: {to_binary(n)}, hex: {to_hexadecimal(n)}")

    elapsed_time = time.time() - start_time
    results.append(f"Execution Time (s): {elapsed_time}")

    # Print to screen
    for line in results:
        print(line)

    # Save to file
    with open("ConvertionResults.txt", "w", encoding="utf-8") as file:
        for line in results:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
