# Knapsack Problem

In this task, you will implement a solution for the **Knapsack Problem** using **recursion**. This problem involves
determining the maximum value achievable by selecting items with given weights and values, without exceeding a specified
weight capacity.

For a fully functional solution, you will receive **4 out of 6 points**. To earn the remaining **2 points**, you must
minimize the number of recursive calls using **dynamic programming** (DP) or a similar optimization approach.

## Task Details

- `capacity`: the maximum weight capacity of the knapsack.
- `weights`: a list of weights for each item.
- `values`: a list of values for each item.
- `lookup_table`: a dictionary or list to store previously computed results for subproblems.

You will implement the function `knapsack(W, weights, values, lookup_table)` that returns the maximum achievable value
without exceeding the `capacity`.

**Output**: The function should return an integer representing the maximum achievable value for the given capacity.

### Constraints

- You **must** use recursion.
- The function **must not contain any loops** (`for` or `while`).
- For full credit (6 points), implement an optimized solution that reduces the number of recursive calls significantly
  by using **dynamic programming** (DP) or memoization. Without this optimization, your score will be capped at 4 out of
  6 points.

## Hints

- **Recursive Case**: Try two possibilities for each item — either include it in the knapsack (if it fits) or exclude
  it — and take the maximum of these choices.
- **Dynamic Programming**: Use a dictionary or list to store results of previously computed subproblems to avoid
  recalculating them, thereby reducing the total number of recursive calls.

## Optional

To learn more about the Knapsack Problem and dynamic programming, you can read the following articles:

- [Knapsack Problem on Wikipedia](https://en.wikipedia.org/wiki/Knapsack_problem#Dynamic_programming)
- [Dynamic Programming in Python](https://realpython.com/python-thinking-recursively/#memoization-and-dynamic-programming)
- You may also want to look at other online resources.
