file_object = open('words.txt')
file_object.readline
import doctest
from doctest import run_docstring_examples
def run_doctests(func):
    run_docstring_examples(func, globals(), name=func.__name__)
def has_e(word):
    return 'e' in word.lower()

total = 0
count = 0

for line in open('words.txt'):
    word = line.strip()
    total = total + 1
    if has_e(word):
        count += 1


def uses_any_incorrect(word, letters):
    """Checks if a word uses any of a list of letters.

    >>> uses_any_incorrect('banana', 'aeiou')
    True
    >>> uses_any_incorrect('apple', 'xyz')
    False
    """
    for letter in word.lower():
        if letter in letters.lower(): return True
    return False  # INCORRECT!

def num_e():
    count = 0
    total = 0
    for line in open('words.txt'):
        word = line.strip()
        total = total + 1
        if has_e(word):
            count += 1
    print(total, count)

num_e()
