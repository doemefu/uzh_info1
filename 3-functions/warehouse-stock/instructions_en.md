You have been tasked with implementing a warehouse stock tracking system.
The system simply records how many of a given product are in stock. Stock can
increase when products are added to the warehouse, and it will decrease if
products are removed from the warehouse, until maybe there is no stock left of
a given product.

Stock is tracked using a Python dictionary. The keys are product names, and the
values are integers indicating how many of the given item are in stock.
Here's an example of what the warehouse dictionary might look like at any given
time:

```
{ "Y-Box Gaming Console": 14,
  "Somsong Flatscreen TV": 11,
  "Logotech Mouse": 251,
  'Dill 13" Laptop': 41,
  "oPhone 15": 881,
  "Nokla 3210": 2
}
```

To manage the warehouse, you need to implement the following functions. Each
of the functions takes a dictionary `warehouse` (structured as outlined above)
as the first parameter.

 * `add_stock(warehouse, product)` increments the stock for the given product by `1`. If the product was not in stock previously, this function will need to add a new key/value pair to `warehouse`.
 * `remove_stock(warehouse, product)` decrements the stock for a given product by `1`. If the product is not in stock, the function should print `"PRODUCT not in stock"` (replace `PRODUCT` with the requested product name). If the product had only `1` remaining in stock, then the key/value pair should be deleted from `warehouse`.
 * `get_stock(warehouse, product)` should return an integer indicating how much stock of the given product is in the warehouse. If the product is not in stock, the function should return `0`


