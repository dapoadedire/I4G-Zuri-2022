# Check if a word is an anagrams 
# Example:
# (is_palindrome("hello") --> False
# (is_palinfrome("racecar") --> True


def is_palindrome(word):
    # [assignment] Add your code here
    # change word to lowercase
    word = word.lower()
    word_palindrome = word[::-1]
    if word == word_palindrome:
        return True
    else:
        return False


print(is_palindrome("Racecar"))
print(is_palindrome("hello"))
print(is_palindrome("redivider"))
print(is_palindrome("deiFied"))
print(is_palindrome("reVivEr"))
print(is_palindrome("thankstobe"))
