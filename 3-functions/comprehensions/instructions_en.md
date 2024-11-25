In this task, you will practice list and dict comprehensions.

In `script.py`, you can find a list of words and six functions. The first function, `words_with_length` has already been implemented as an example. It takes a parameter `length` and returns only those words which have this given length.

The other functions are for you to implement. Remember that you can always add `print` statements at the bottom to call your implementation, for example:

```
print(words_with_length(5))
```

**Important:** all functions *must* start with a `return` statement and they *must* return a list or dict comprehension, just as demonstrated in `words_with_length`. Replace `pass` with your return statement; do not declare any variables; construct and return a comprehension outright.

Implement the following 5 functions:

* `words_containing_string(s)` should return a list of all those words from `words` which contain the given string `s`.

* `words_starting_with_character(c)` should return a list of all those words from `words` which start with the given character `c`.

* `words_with_matching_ends()` should return a list of all those words where the first and last character are the same.

* ` words_with_unique_characters()` should return a list of all those words, in which each individual character only appears once. For example, this would be true for "peach", but false for "apple", because the latter contains two 'P's.

* `count_unique_characters()` should return a dictionary, where the keys are the words and the values are integers indicating how many unique characters the word contains.

* `dictionary()` should return a dictionary where each key-value pair consists of a letter of the alphabet as the key, and a list of all the words starting with the corresponding character as its value. So for example `dictionary()["a"]` should contain the list of all words starting with "a". You can call your function `words_starting_with_character` to get a list of words starting with a specific character. To get a string containing all alphabetic characters, you can import `ascii_lowercase` from the `string` module (do this at the top of `script.py`, not within your function). Naturally, if there aren't any words starting with a given character, the value for that key should be the empty list, meaning that the return value of `dictionary` will always be a dictionary containig 26 key/value pairs, no matter what. Note that the solution may be unexpectedly trivial.

