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
