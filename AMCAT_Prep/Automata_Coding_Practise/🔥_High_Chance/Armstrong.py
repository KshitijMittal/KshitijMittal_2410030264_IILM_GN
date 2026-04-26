'''
Check Armstrong Number

Theory: An Armstrong number (also known as a narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits. For example, 153 is an Armstrong number because it has 3 digits and 1³ + 5³ + 3³ = 153.

Problem: An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself. Return true if the given number is an Armstrong number.

Example 1:
Input: num = 153
Output: true
Explanation: 1³ + 5³ + 3³ = 1 + 125 + 27 = 153

Example 2:
Input: num = 123
Output: false

Constraints: 0 <= num <= 10^9
'''

class Solution:
    def isArmstrong(self, num: int) -> bool:
        # Convert the number to a string to iterate through its digits
        num_str = str(num)
        n = len(num_str)  # Get the number of digits

        # Calculate the sum of the digits raised to the power of n
        armstrong_sum = sum(int(digit) ** n for digit in num_str)

        # Check if the calculated sum is equal to the original number
        return armstrong_sum == num

# Get user input
number = int(input("Enter a number: "))
# Create an instance of the Solution class
solution = Solution()
# Check if the number is an Armstrong number and print the result
if solution.isArmstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")