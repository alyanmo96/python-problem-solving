"""
    Checks whether a given string is a palindrome.

    A palindrome is a word, phrase, or sequence that reads the same backward as forward.
  """
def is_palindrome(s):
    return s==s[::-1]


# Example usage
print(is_palindrome('a'))     # True
print(is_palindrome('aba'))   # True
print(is_palindrome('abca'))  # False