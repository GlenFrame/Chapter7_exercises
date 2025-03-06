# asking a virtual assistant
import doctest
from doctest import run_docstring_examples

def run_doctests(func):
    run_docstring_examples(func, globals(), name=func.__name__)

"""The issue with your function is that it returns False as soon as it finds a letter in word that is not in letters, without checking the rest of the word. This causes incorrect results because the function will stop prematurely instead of examining all letters.

What Happens?
If the first letter of word is not in letters, it returns False immediately.
If the first letter is in letters, it returns True immediately—without checking the remaining letters.
Example of Incorrect Behavior
python
Copy
Edit
print(uses_any_incorrect("hello", "h"))  # Returns True (incorrect)
print(uses_any_incorrect("hello", "xyz"))  # Returns False (correct)
print(uses_any_incorrect("hello", "el"))  # Returns True (incorrect, should be False)
How to Fix It
You should return True if any letter in word is found in letters, but only return False after checking all letters.

Corrected Version
python
Copy
Edit
def uses_any_incorrect(word, letters):
    for letter in word.lower():
        if letter in letters.lower():
            return True  # Return True if any letter is found
    return False  # Only return False if no letter was found
Why This Works
The function iterates through all letters in word.
If at least one letter is in letters, it immediately returns True.
If none of the letters are in letters, it returns False after the loop finishes.
Correct Behavior Now
python
Copy
Edit
print(uses_any_incorrect("hello", "h"))  # True (correct)
print(uses_any_incorrect("hello", "xyz"))  # False (correct)
print(uses_any_incorrect("hello", "el"))  # True (correct)
print(uses_any_incorrect("world", "z"))  # False (correct)
This properly checks all letters before deciding on False"""
from Practice import run_doctests


def uses_none(word, forbidden): # both of our methods word, I don't see much of a difference but maybe an advanced coder would say otherwise.
    """Checks whether a word avoid forbidden letters.

    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    >>> uses_none('kitchen', 'aou')
    True
        """
    for letter in word.lower():
        if letter in forbidden.lower():
            return False
    return True


def uses_any(word, letters): #
    """Checks if a word uses any of a list of letters.

    >>> uses_any('banana', 'aeiou')
    True
    >>> uses_any('apple', 'xyz')
    False
    """
    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False

def uses_only(word, available): # once again, I don't see much of a difference. Maybe I could have improved mine by adding a variable for lowercase instead of using .lower() each time
    """Checks whether a word uses only the available letters.

    >>> uses_only('banana', 'ban')
    True
    >>> uses_only('apple', 'apl')
    False
    >>> uses_only('mississippi', 'mspi')
    True
    >>> uses_only('rhomboid', 'iodbrh')
    False
    """
    for letter in word.lower():
        if letter not in available.lower():
           return False
    return True


def uses_all(word, required): # Mine is kinda ugly. I don't like it. I just messed around until something worked to be honest. I could improve the execution and layout of the code.
    """Checks whether a word uses all required letters.

    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    >>> uses_all('atlas','lats' )
    True
    >>> uses_all('abcdefghijk', 'abcdefghijklmnopqrstuvwxyz')
    False
    >>> uses_all('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuv')
    True
    """
    if all(letter in word.lower() for letter in required.lower()):
        return True
    return False


def check_word(word, available, required): # mine works and is easier to understand, so I'm not sure what to say... but I do think it might be inefficient for two functions to be called instead of just one.
    """Check whether a word is acceptable.

    >>> check_word('color', 'ACDLORT', 'R')
    True
    >>> check_word('ratatat', 'ACDLORT', 'R')
    True
    >>> check_word('rat', 'ACDLORT', 'R')
    False
    >>> check_word('told', 'ACDLORT', 'R')
    False
    >>> check_word('bee', 'ACDLORT', 'R')
    False
    """
    if 3 < len(word) <= 7:
        if uses_only(word, available):
            return uses_all(word, required)
    return False


def word_score(word, available): # My simple brain likes mine better, but the professors is more... professional looking. I think that his is better and mine should be improved to be cleaner
    """Compute the score for an acceptable word.

    >>> word_score('card', 'ACDLORT')
    1
    >>> word_score('color', 'ACDLORT')
    5
    >>> word_score('cartload', 'ACDLORT')
    15
    """
    length = len(word)
    if length == 4:
        return 1
    elif uses_all(word, available):
        return length + 7
    else:
        return length

def uses_all_improved(word, required): # they are the same, no way to improve it unless I somehow improved uses_only because all it does is call that function.
    """Checks whether a word uses all required letters.

    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    >>> uses_all('atlas','lats' )
    True
    >>> uses_all('abcdefghijk', 'abcdefghijklmnopqrstuvwxyz')
    False
    >>> uses_all('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuv')
    True
    """
    return uses_only(required, word)

def uses_all_gpt(word, required): # mine seems more efficient than the professors version of the gpt prompt, so I would say that my ChatGPT was smarter... hhm I wonder why, it's almost like they update it every few months....
    """Checks whether a word uses all required letters.

    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    >>> uses_all('atlas','lats' )
    True
    >>> uses_all('abcdefghijk', 'abcdefghijklmnopqrstuvwxyz')
    False
    >>> uses_all('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuv')
    True
    """
    return all(uses_any(word, letter) for letter in required)


print(uses_none("kitchen", "aou"))

# Fun assignment :))) Now I want to create a program that automatically does the nyt spelling bee using the word library.