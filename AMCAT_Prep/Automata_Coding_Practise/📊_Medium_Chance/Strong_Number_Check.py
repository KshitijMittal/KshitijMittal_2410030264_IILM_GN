'''
Strong Number Check

Theory: A strong number (or factorial number) is one where the sum of factorials of its digits equals the number itself. For example, 145 is strong because 1! + 4! + 5! = 1 + 24 + 120 = 145.

Problem: Return true if the given number is a strong number, otherwise return false.

Example 1:
Input: num = 145
Output: true
Explanation: 1! + 4! + 5! = 1 + 24 + 120 = 145

Example 2:
Input: num = 123
Output: false

Constraints: 1 <= num <= 10^6
'''

class Solution:
    def isStrong(self, num: int) -> bool:
        # Precompute factorials for digits 0-9
        factorials = [1] * 10
        for i in range(2, 10):
            factorials[i] = factorials[i - 1] * i

        # Calculate the sum of factorials of the digits
        strong_sum = sum(factorials[int(digit)] for digit in str(num))

        # Check if the calculated sum is equal to the original number
        return strong_sum == num

# Get user input
number = int(input("Enter a positive integer: "))
# Create an instance of the Solution class
solution = Solution()
# Check if the number is a strong number and print the result
if solution.isStrong(number):
    print(f"{number} is a strong number.")
else:
    print(f"{number} is not a strong number.")
