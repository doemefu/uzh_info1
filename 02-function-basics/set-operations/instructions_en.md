In the lecture, you've heard about tuples, lists and sets, and how to create them:

```
my_tuple = (1, "a", 1, 2)  # my_tuple is going to be (1, 'a', 1, 2)
my_list = [1, "a", 1, 2]   # my_list is going to be  [1, 'a', 1, 2]
my_set = {1, "a", 1, 2}    # my_set is going to be   {'a', 1, 2}
```

These data structures can also be created from each other using the `tuple`, `list` and `set` functions:

```
another_set = set(my_tuple)    # another_set is going to be   {1, 'a', 2}
another_list = list(my_tuple)  # another_list is going to be  [1, 'a', 1, 2]
another_tuple = tuple(my_set)  # another_tuple is going to be ('a', 1, 2)
```

With this new knowledge, implement a function `list_unique` which takes a **tuple** of arbitrary elements `elements` as the only parameter and returns a **list** containing only the unique elements contained in `elements`. The ordering of the elements in the return value does not matter.

For example, given elements `(1, 2, 2, 3, 4, 5, 5, "Hi!")` the result should be a list `[1, 2, 3, 4, 5, 'Hi!']` (in any order).

**Sidenote**: You might notice that you cannot make a set from a list that contains another list: `set([1,2,["a nested list", 3, 4]])` will give you a `TypeError: unhashable type: 'list'`. We'll discuss what this means in a later lecture.
