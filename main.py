#!/bin/env python3

with open('books/frankenstein.txt') as f:
    file_contents = f.read()

def count_words(text):
    return len(text.split())
