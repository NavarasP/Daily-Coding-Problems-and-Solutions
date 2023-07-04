# **📌 DCP-1** 

Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number `k`, return whether any two numbers from the list add up to `k`.

For example, given `[10, 15, 3, 7]` and `k` of `17`, return true since `10 + 7` is `17`.

# **⭐ SOLUTION** 

This code snippet is written in Python and demonstrates the `find_pair` function. It takes a list of numbers `numbers` and a target sum `k` as input. The function uses a hash set `seen_numbers` to keep track of the numbers encountered during the iteration. It iterates through each number in the list and checks if the complement (the difference between the target sum and the current number) is already present in the set. If a pair of numbers that add up to `k` is found, it returns a string stating the pair of numbers along with the `seen_numbers` set. If no pair is found, it returns the string "Not Found". Finally, the function is invoked with the provided example inputs and the output is printed.

I hope this clarifies the code snippet for you. Let me know if you have any further questions!
