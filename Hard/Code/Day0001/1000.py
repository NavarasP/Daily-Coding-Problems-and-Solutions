def array_product(arr):
    product = 1
    for num in arr:
        product *= num
    return product


def calculate_products_except_self(array):
    product = array_product(array)
    result = []
    for num in array:
        result.append(product // num)
    return result


array = [1, 2, 3, 4, 5]
result = calculate_products_except_self(array)
print("Result:", result)
