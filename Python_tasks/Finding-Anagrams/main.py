# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

import re
def find_anagram(word, anagram):
    # [assignment] Add your code here

    # remove all whitespace characters and convert to lowercase.
    word = word.replace(" ", "").lower()
    anagram = anagram.replace(" ", "").lower()

    if sorted(word.lower()) == sorted(anagram.lower()):
        return True
    else:
        return False
print(find_anagram("hello", "check"))
print(find_anagram("below", "elbow"))

