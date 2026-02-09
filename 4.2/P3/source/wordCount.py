#!/usr/bin/env python3
"""
wordCount.py

Counts distinct words in a text file and their frequencies.
"""

import sys
import time


def read_words(file_path):
    """Read words from a file, handle invalid lines."""
    words = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue
                try:
                    # Split line by spaces
                    line_words = line.split()
                    words.extend(line_words)
                except Exception:
                    print(f"Invalid data at line {line_number}: '{line}'")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)
    return words


def count_words(words):
    """Count frequency of each distinct word using basic algorithms."""
    word_list = []
    freq_list = []

    for word in words:
        if word in word_list:
            idx = word_list.index(word)
            freq_list[idx] += 1
        else:
            word_list.append(word)
            freq_list.append(1)

    return word_list, freq_list


def main():
    """Main program."""
    if len(sys.argv) < 2:
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)

    start_time = time.time()
    file_path = sys.argv[1]

    words = read_words(file_path)

    if not words:
        print("No valid words found.")
        sys.exit(1)

    distinct_words, frequencies = count_words(words)

    results = []
    for word, freq in zip(distinct_words, frequencies):
        results.append(f"{word} -> {freq}")

    elapsed_time = time.time() - start_time
    results.append(f"Execution Time (s): {elapsed_time}")

    # Print to screen
    for line in results:
        print(line)

    # Save to file
    with open("WordCountResults.txt", "w", encoding="utf-8") as file:
        for line in results:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
