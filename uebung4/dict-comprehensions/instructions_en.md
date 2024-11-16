In this task, you will take a closer look at the possibilities of dict comprehensions.

In `script.py`, you can find a list of numbers and four functions. The target of these functions is to generate lookup dictionaries for numeric operations which could help to save computation time if calculations with certain numbers are done regularly. For each number the results of these calculations are then safed in a dictionary. 

The first function `square_root_dict` is an example how dict comprehension should look like. The function returns a dictionary with a number as key and the square root as value. 

**Important:** all functions *must* start with a `return` statement and they *must* return a dict comprehension, just as demonstrated in ``. Replace `pass` with your return statement; do not declare any variables; construct and return a comprehension outright.

Please implement the following functions 

* The second function `even_odd_dict` shall return a dictionary that contains the numbers as keys and for each number 'event' or 'odd' as value. 

```
numbers = [1, 2, 3]

# Expected return value:
{
    -2: 'even'
    1: 'odd',
    2: 'even',
    3: 'odd'
}
```

* The third function `area_dict` shall return a dictionary that contains the previously mentioned numbers as keys and another dictionary as value. The value dictionary shall contain the area of a square with the number as side lenght, the area of a circle with the number as radius. However only non-negative numbers shall have entries in the area dictionary. `pi` has been imported from `math` for the circle area calculation (r^2*pi).

```
numbers = [-1, 1, 2, 3]

# Expected return value:
{
    1: {
        'square': 1,
        'circle': 3.141592653589793
    },
    2: {
        'square': 4,
        'circle': 12.566370614359172
    },
    3: {
        'square': 9,
        'circle': 28.274333882308138
    }
}
```

* The last function `smaller_larger_dict` shall return a dictionary that has the numbers as keys and another dictionary as value. In this value dictionary every other number is a key and the value tells if the number is 'smaller' or 'larger' as the first key. The first key itself shall not be contained in the value dictionary.

```
numbers = [-1, 1, 2]

# Expected return value:
{
    -1: {
        1: 'larger',
        2: 'larger'
    },
    1: {
        -1: 'smaller',
        2: 'larger'
    },
    2: {
        -1: 'smaller',
        1: 'smaller'
    },
}
```
