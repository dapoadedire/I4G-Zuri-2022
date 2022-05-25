def is_palindrome(string):
    string = string.lower()

    rev_string = reversed(string)

    if list(string) == list(rev_string):
        print("The string is a palindrome")

    else:
        print("The string is not a palindrome")


is_palindrome("Racecar")
is_palindrome("hello")