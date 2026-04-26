'''
Even Odd Check

Theory: A number is even if divisible by 2 (num % 2 == 0), odd otherwise. Single bitwise operation (num & 1) also works (last bit 0=even, 1=odd).

Problem: Given an integer num, return "Even" if even, "Odd" if odd.

Example 1:
Input: num = 4
Output: "Even"

Example 2:
Input: num = 7
Output: "Odd"

Constraints: 0 <= num <= 10^9
'''

class Solution:
    def evenOdd(self, num: int) -> str:
        # Check if the number is even or odd using bitwise operation
        if num & 1 == 0:  # If the last bit is 0, it's even
            return "Even"
        else:             # If the last bit is 1, it's odd
            return "Odd"

# Get user input
number = int(input("Enter an integer: "))
# Create an instance of the Solution class
solution = Solution()
# Check if the number is even or odd and print the result
result = solution.evenOdd(number)
print(f"{number} is {result}.")
