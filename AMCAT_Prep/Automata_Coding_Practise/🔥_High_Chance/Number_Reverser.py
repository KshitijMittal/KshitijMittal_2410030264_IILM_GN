'''
Number Reverser

Theory: Reversing a number involves extracting digits (using %10 and /10) and rebuilding in reverse order, handling carry-over for potential overflow.

Problem: Given a positive integer num, return its reverse (without leading zeros).

Example 1:
Input: num = 123
Output: 321

Example 2:
Input: num = 120
Output: 21

Constraints: 0 <= num <= 10^9
'''

class Solution:
    def reverseNumber(self, num: int) -> int:
        reversed_num = 0
        while num > 0:
            digit = num % 10  # Get the last digit
            reversed_num = reversed_num * 10 + digit  # Append the digit to the reversed number
            num //= 10  # Remove the last digit from num

        return reversed_num

# Get user input
number = int(input("Enter a positive integer: "))
# Create an instance of the Solution class
solution = Solution()
# Get the reversed number and print the result
reversed_number = solution.reverseNumber(number)
print(f"The reverse of {number} is {reversed_number}.")
