def power_set(nums):
    def backtrack(start, current_subset):
        power_set.append(current_subset[:]) 
        for i in range(start, len(nums)):
            current_subset.append(nums[i])
            backtrack(i + 1, current_subset)
            current_subset.pop()

    power_set = []
    backtrack(0, [])
    return power_set


input_set = [1, 2, 3]
result = power_set(input_set)
print(result)
