'''
Swap Without Temp Variable

Theory: Two numbers can be swapped without temp using arithmetic (a=a+b, b=a-b, a=a-b) or XOR (a=a^b, b=a^b, a=a^b). Both O(1) space.

Problem: Swap two integers a and b without using a temporary variable and return them as a list.

Example 1:
Input: a = 5, b = 10
Output: [10, 5]

Example 2:
Input: a = 1, b = 1
Output: [1, 1]

Constraints: 0 <= a, b <= 10^9
'''

class Solution:
    def swapNumbers(self, a: int, b: int) -> list[int]:
        # Swap using arithmetic operations
        a = a + b  # Step 1: a now holds the sum of a and b
        b = a - b  # Step 2: b now holds the original value of a
        a = a - b  # Step 3: a now holds the original value of b

        return [a, b]


# Get user input
a = int(input("Enter the first integer (a): "))
b = int(input("Enter the second integer (b): "))
# Create an instance of the Solution class
solution = Solution()
# Swap the numbers and print the result
swapped_result = solution.swapNumbers(a, b)
print(f"After swapping: a = {swapped_result[0]}, b = {swapped_result[1]}")
