'''
Palindrome Number Check

Theory: A palindromic number reads the same backward as forward. For example, 121 is a palindrome because it equals 121 when reversed.

Problem: Given a positive integer num, return true if it reads the same backward as forward, otherwise return false.

Example 1:
Input: num = 121
Output: true
Explanation: 121 reads the same backward as forward

Example 2:
Input: num = 123
Output: false

Constraints: 0 <= num <= 10^9
'''

class Solution:
    def isPalindrome(self, num: int) -> bool:
        # Convert the number to a string to check for palindrome
        num_str = str(num)

        # Check if the string is equal to its reverse
        return num_str == num_str[::-1]

# Get user input
number = int(input("Enter a positive integer: "))
# Create an instance of the Solution class
solution = Solution()
# Check if the number is a palindrome and print the result
if solution.isPalindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
