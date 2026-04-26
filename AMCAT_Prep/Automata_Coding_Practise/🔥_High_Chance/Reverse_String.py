'''
Reverse String

Theory: Reversing a string means changing the order of characters so the last character becomes first, second-to-last becomes second, etc. For "hello", the reverse is "olleh".

Problem: Given a string s, reverse the string and return the reversed string.

Example 1:
Input: s = "hello"
Output: "olleh"

Example 2:
Input: s = "racecar"
Output: "racecar"
Explanation: "racecar" is a palindrome

Constraints: 1 <= s.length <= 1000, s contains only lowercase English letters
'''

class Solution:
    def reverseString(self, s: str) -> str:
        # Reverse the string using slicing
        return s[::-1]

# Get user input
input_string = input("Enter a string: ")
# Create an instance of the Solution class
solution = Solution()
# Reverse the input string and print the result
reversed_string = solution.reverseString(input_string)
print(f"The reversed string is: {reversed_string}")
