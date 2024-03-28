# **📌 DCP-1000** 

Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index `i` of the new array is the product of all the numbers in the original array except the one at `i`.

For example, if our input was `[1, 2, 3, 4, 5]`, the expected output would be `[120, 60, 40, 30, 24]`. If our input was `[3, 2, 1]`, the expected output would be `[2, 3, 6]`.

# **⭐ SOLUTION** 


The provided code calculates the product of all elements in an array and creates a new array where each element is the product of all other elements except the current element. This is commonly known as finding the "product of array except self."

## `array_product(arr)`

This function calculates the product of all elements in an array. It takes an array `arr` as input.

- `arr`: The input array for which the product needs to be calculated.

The function works as follows:

1. Initializes a variable `product` to 1.
2. Iterates over each element `num` in the input array `arr`.
3. For each element, multiplies `product` by `num` and updates the `product` variable.
4. Finally, returns the calculated `product` as the result of the function.

## `calculate_products_except_self(array)`

This function takes an array `array` as input and calculates the product of all elements except the current element.

- `array`: The input array for which the product needs to be calculated.

The function works as follows:

1. Calls the `array_product` function, passing the input array `array`, to calculate the product of all elements. The result is stored in the `product` variable.
2. Initializes an empty list `result` to store the resulting products of all elements except the current element.
3. Iterates over each element `num` in the input array `array`.
4. For each element, calculates the product by dividing the total `product` by the current element `num` using integer division (`//`). This gives the product of all other elements except the current element.
5. Appends the calculated product to the `result` list.
6. Finally, returns the `result` list as the output of the function.

## Usage

```python
array = [1, 2, 3, 4, 5]
result = calculate_products_except_self(array)
print("Result:", result)
