# Recursive Palindrome Checker

In this task, you will implement a function to determine if a given string is a palindrome using **recursion**. A *
*palindrome** is a word, phrase, or sequence that reads the same backward as forward, ignoring spaces, punctuation, and
case.

## Task Details

Given a string `s`, implement the function `is_palindrome(s)` which should return `True` if `s` is a palindrome and
`False` otherwise. Your function should ignore all non-alphanumeric characters and should not differentiate between
uppercase and lowercase letters.

### Examples of Palindromes

- A man, a plan, a canal: Panama
- No lemon, no melon

### Constraints

- You **must** use recursion for this task.
- The function **must not contain any loops** (`for` or `while`).
- You should not use any additional helper functions outside of `is_palindrome`.

## Hints

- **Cleaning the String**: You can use the `re.sub` function from Python’s `re` module to remove all non-alphanumeric
  characters and convert the string to lowercase.

## Optional

- To learn more about the `re` module, you can read the following
  article: [Regular Expression Operations](https://docs.python.org/3/library/re.html).
