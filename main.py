#!/bin/env python3

file_name = "books/frankenstein.txt"

with open(file_name) as f:
    file_contents = f.read()

def count_words(text):
    return len(text.split())
