#!/usr/bin/env python3
"""
computeStatistics.py

Computes descriptive statistics from a file containing numbers.
Statistics: mean, median, mode, variance, standard deviation.
"""

import sys
import time


RESULTS_FILE = "StatisticsResults.txt"


def read_numbers(file_path):
    """Read numbers from a file, handling invalid data."""
    numbers = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            value = line.strip()

            if not value:
                continue

            try:
                numbers.append(float(value))
            except ValueError:
                print(
                    f"Invalid data at line {line_number}: '{value}'"
                )

    return numbers


def mean(numbers):
    """Calculate mean."""
    total = 0.0
    count = 0

    for num in numbers:
        total += num
        count += 1

    return total / count


def median(numbers):
    """Calculate median."""
    sorted_numbers = sorted(numbers)
    count = len(sorted_numbers)
    middle = count // 2

    if count % 2 == 0:
        return (
            sorted_numbers[middle - 1]
            + sorted_numbers[middle]
        ) / 2

    return sorted_numbers[middle]


def mode(numbers):
    """Calculate mode."""
    frequency = {}

    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    max_count = 0
    modes = []

    for num, count in frequency.items():
        if count > max_count:
            max_count = count
            modes = [num]
        elif count == max_count:
            modes.append(num)

    if max_count == 1:
        return None

    return modes


def variance(numbers, avg):
    """Calculate variance."""
    total = 0.0
    count = 0

    for num in numbers:
        diff = num - avg
        total += diff * diff
        count += 1

    return total / count


def standard_deviation(var):
    """Calculate standard deviation."""
    return var ** 0.5


def write_results(results):
    """Write results to output file."""
    with open(RESULTS_FILE, "w", encoding="utf-8") as file:
        for line in results:
            file.write(line + "\n")


def main():
    """Main execution function."""
    if len(sys.argv) < 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        sys.exit(1)

    start_time = time.time()
    file_path = sys.argv[1]

    numbers = read_numbers(file_path)

    if not numbers:
        print("No valid numeric data found.")
        sys.exit(1)

    avg = mean(numbers)
    med = median(numbers)
    mod = mode(numbers)
    var = variance(numbers, avg)
    std_dev = standard_deviation(var)

    elapsed_time = time.time() - start_time

    results = [
        f"Count: {len(numbers)}",
        f"Mean: {avg}",
        f"Median: {med}",
        f"Mode: {mod}",
        f"Variance: {var}",
        f"Standard Deviation: {std_dev}",
        f"Execution Time (s): {elapsed_time}",
    ]

    for line in results:
        print(line)

    write_results(results)


if __name__ == "__main__":
    main()
