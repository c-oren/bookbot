#!/bin/env python3

file_name = "books/frankenstein.txt"

with open(file_name) as f:
    file_contents = f.read()

def count_words(text):
    return len(text.split())

def count_letters(text):
    letter_counts = {}

    for l in text.lower():
        if l.isalpha():
            letter_counts[l] = letter_counts.get(l, 0) + 1

    return letter_counts

def report():
    print(f"--- Begin report of {file_name} ---")
    print(f"{count_words(file_contents)} words found in the document\n")

    ltr_count = list(count_letters(file_contents).items())
    ltr_count.sort(key=lambda x: x[1], reverse=True)

    for k, v in ltr_count:
        print(f"The '{k}' character was found {v} times")

    print("--- End report ---")

report()
