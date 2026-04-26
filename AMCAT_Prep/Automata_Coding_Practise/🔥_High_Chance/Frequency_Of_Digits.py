'''
Digit Frequency Counter

Theory: Given a number and a specific digit, we need to count how many times that digit appears in the number's decimal representation.

Problem: Given a positive integer num and a digit digit (0-9), return the count of digit's occurrences in num.

Example 1:
Input: num = 12213, digit = 2
Output: 2
Explanation: Digit 2 appears twice in 12213

Example 2:
Input: num = 2591, digit = 5
Output: 1

Constraints: 0 <= num <= 10^9, 0 <= digit <= 9
'''

class Solution:
    def digitFrequency(self, num: int, digit: int) -> int:
        # Convert the number to a string to iterate through its digits
        num_str = str(num)
        digit_str = str(digit)  # Convert the digit to a string for comparison

        # Count the occurrences of the digit in the number
        frequency = num_str.count(digit_str)

        return frequency

# Get user input
number = int(input("Enter a number: "))
digit = int(input("Enter a digit (0-9): "))
# Create an instance of the Solution class
solution = Solution()
# Get the frequency of the digit in the number and print the result
frequency = solution.digitFrequency(number, digit)
print(f"The digit {digit} appears {frequency} times in the number {number}.")
