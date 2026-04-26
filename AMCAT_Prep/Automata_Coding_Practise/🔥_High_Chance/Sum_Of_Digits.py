'''
Sum of Digits

Theory: Sum of digits extracted by repeated modulo 10 (%10 gives last digit) and integer division 10 (/10 removes last digit). Continue until num becomes 0.

Problem: Given a non-negative integer num, return the sum of its digits.

Example 1:
Input: num = 38
Output: 11
Explanation: 3 + 8 = 11

Example 2:
Input: num = 0
Output: 0

Constraints: 0 <= num <= 10^18
'''

class Solution:
    def sumOfDigits(self, num: int) -> int:
        total_sum = 0
        while num > 0:
            total_sum += num % 10  # Add the last digit to the total sum
            num //= 10  # Remove the last digit from num
        return total_sum

# Get user input
number = int(input("Enter a non-negative integer: "))
# Create an instance of the Solution class
solution = Solution()
# Calculate the sum of digits and print the result
result = solution.sumOfDigits(number)
print(f"The sum of the digits in the number {number} is: {result}.")
