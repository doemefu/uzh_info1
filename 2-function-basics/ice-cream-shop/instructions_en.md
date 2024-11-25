Assume that you are writing the cashier software for an ice cream shop.

The shop offers two types of ice cream: vanilla and chocolate. An order always consists of exactly one cone and any number of scoops.

To make your calculation logic extendable, all prices and the number of ordered scoops can be configured through variables (i.e., `num_scoops_...` and `price_...`). The total price of an order is calculated by a function called `get_price`. For example, given a cone price of 0.50 and a price per scoop of 1.20 for both vanilla and chocolate, an order of 2 scoops vanilla and 1 scoop chocolate would translate to the following call: `get_price(0.50, 2, 1.20, 1, 1.20)`.

Implement `get_price`.

Please make sure that your solution is self-contained within the `get_price` function. In other words, only change the body of the function, not the code outside the function.

By the way: you need not and *should not* use `input` in this exercise. This is a common point of confusion. `input` is only used when creating *interactive* applications, where the user interacts with the program. In this task, the variables are already set to the given values in the source code. You can change these values in the source code (as the price of different products changes), but you cannot and should not be using `input` to create an interactive program.

