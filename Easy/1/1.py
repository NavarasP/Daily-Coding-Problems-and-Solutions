def find_pair(numbers, k):
    seen_numbers = set()

    for num in numbers:
        complement = k - num
        if complement in seen_numbers:
            return f"Numbers are {num} and {complement}", seen_numbers
        seen_numbers.add(num)

    return "Not Found"

numbers = [10, 15, 3, 7]
k = 17

output = find_pair(numbers, k)
print(output)
