"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here

    # Iterate through items
    for item in items:
        # Deal with non-string items
        if not isinstance(item, str):
            key = str(item)

        # Look to next key and add current key to dictionary
        frequencies[key] = frequencies.get(key, 0) + 1

    # Return dictionary
    return frequencies
