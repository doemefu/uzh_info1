In this task, you will write a data structure `Publication` that can be used to represent scientific articles. In a simplified form, such an article has a *list of authors* (assume that only last names are used), a *title*, and a *year* of publication. For example:

```python
    references = [
        Publication(["Gamma", "Helm", "Johnson", "Vlissides"], "Design Patterns", 1994),
        Publication(["Cockburn"], "Writing Effective Use Cases", 2000),
        Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    ]
```

First of all, it must be easy to explore such values, be it by printing or by looking at them in a debugger. To make this work, it is necessary to provide the two methods [\__repr__](https://docs.python.org/3.5/reference/datamodel.html#object.__repr__) and [\__str__](https://docs.python.org/3.5/reference/datamodel.html#object.__str__). For this task, the representation of both should be the same as the string required for the instantiation. More specifically:

```python
    p = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    s = """Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)"""
    assert str(p) == s
```

### Rich comparison operators and `NotImplemented`

The next important property of a data structure is that is is possible to identify equal values. To allow that, a data structure has to implement the special method [\__eq__](https://docs.python.org/3.5/reference/datamodel.html#object.\_\_eq\_\_) and, by extension, also [\__hash__](https://docs.python.org/3.5/reference/datamodel.html#object.__hash__).

When implementing comparison operators, one may make the assumption that a user of your class will only ever compare objects of the same type. However, to prevent problems when a user compares values of your custom type to other, unsupported values, it is recommended to `return NotImplemented` from each of the rich comparison operators. We've provided an example for this in `task/script.py` for the `__le__` operator. **Important**: `NotImplemented` is *not* an exception or warning, it is just a special value. As such, it is **returned** not raised.

Implement both methods and make sure that `__eq__` does not crash when compared with types that are not `Publication`. Once these methods are implemented, it is possible to use the `==` operator, e.g., when asserting for the expected output in a test.

```python
    p1 = Publication(["A"], "B", 1234)
    p2 = Publication(["A"], "B", 1234)
    p3 = Publication(["B"], "C", 2345)
    print(p1 == p2) # True
    print(p2 == p3) # False
```

### "Private" instance attributes

Many programming languages support the concept of "private" attributes. Python also supports this (even if in a very soft manner): if you prepend two underscores (`__`) to a class attribute or method, it becomes "private" and cannot be (directly) accessed from the outside anymore. Consider this example:

```python
class A:
    def __init__(self, thing):
        self.thing = thing

a = A("something")
print(a.thing)                       # Works normally

class B:
    def __init__(self, thing):
        self.__thing = thing         # __thing is "private"

b = B("something")
print(b.thing)                       # Crashes with AttributeError: 'B' object has no attribute 'thing'
print(b.__thing)                     # Crashes with AttributeError: 'B' object has no attribute '__thing'. Did you mean: '_B__thing'?
```

In the example above, `__thing` is a "private" attribute of B and cannot be directly accessed anymore. This is useful to discourage users of your class from modifying attributes that they're not supposed to modify. However, note that it is still possible to modify "private" members in Python this in a round-about way by accessing `_B__thing` instead. So in Python, this is really just a soft wall that can be broken down easily, but it does help inform the user of your class that they're not supposed to do this.

### Revealing private attributes via getter methods

Being hashable is required when objects should serve as dictionary keys. In addition, it is also required that such objects are immutable. This means that the different `Publication` attributes must not be stored in public instance attributes. These could be changed from the outside, which would change their hash value uncontrollably. To solve this issue, store the attributes in "private" instance attributes (e.g., `__title`) and only provide public *getter* methods that allow indirect, read-only access (i.e., `get_authors`, `get_title`, `get_year`). This can be more tricky than you might think at first glance. For example, you need to make sure that you do not directly expose the list of authors, because it is mutable and could be changed by users! In other words, if you simply return `__authors` from your `get_authors` method, then the actual list object will be exposed, since `get_authors` only returns a reference to, not a copy of `__authors`.

Once you made `Publication` immutable, it can safely be used as a dictionary key:

```python
    sales = {
        p1: 273,
        p3: 398,
    }
```

### Remaining rich comparison operators

Last, but not least, data structures can implement various special methods that are used by the comparison operators (i.e., [<](https://docs.python.org/3.5/reference/datamodel.html#object.__lt__), [<=](https://docs.python.org/3.5/reference/datamodel.html#object.__le__), [>](https://docs.python.org/3.5/reference/datamodel.html#object.__gt__), [>=](https://docs.python.org/3.5/reference/datamodel.html#object.__ge__)). Implement these methods to make `Publication` comparable. The sorting should be performed according to the following rules:

* First compare the list of authors names, e.g., `["A"] < ["B"]` and `["A", "B"] < ["A", "C"]`. You don't actually need to implement this yourself; just compare the ordered lists using the implementation provided by Python. You may want to learn about how it works by trying different comparisons in a Python interpreter.
* If the author list is identical, compare titles with standard string comparison.
* Otherwise, compare years with standard int comparison.

All *six* comparison operators should *return* boolean values (or the `NotImplemented` *value* when called with a non-`Publication` object as the second parameter). Be smart and think about the relation of the various comparisons. A smart implementation only supports some base cases and delegates the remaining comparisons to these base cases. Once all methods are implemented, it is possible to use the comparison operators (e.g., `p1 < p3`) or to use other utilities like `sorted(references)`.

**Note:** We encourage you to play around with your data structure to understand the effect that providing the various methods has on the way in which you can use your data structure.

**Note:** All state must be contained within the class. Do not store information in global variables or in class variables. It has to be possible to use multiple instances of the classes in parallel without suffering from side effects.

**Note:** The provided files define the signatures of various classes and functions. Do not change these signatures or the automated grading will fail.

**Note:** We strongly encourage you to add more tests to the public test suite.


