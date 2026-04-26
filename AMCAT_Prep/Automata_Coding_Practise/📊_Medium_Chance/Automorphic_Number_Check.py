'''
Automorphic Number Check

Theory: An automorphic number is one whose square ends with the number itself. For example, 25 is automorphic because 25² = 625 (ends with 25), and 76 because 76² = 5776 (ends with 76).

Problem: Return true if the given number is automorphic (its square ends with itself).

Example 1:
Input: num = 25
Output: true
Explanation: 25² = 625 (ends with 25)

Example 2:
Input: num = 13
Output: false
Explanation: 13² = 169 (does not end with 13)

Constraints: 0 <= num <= 10^5
'''

class Solution:
    def isAutomorphic(self, num: int) -> bool:
        # Calculate the square of the number
        square = num ** 2

        # Convert both the number and its square to strings
        num_str = str(num)
        square_str = str(square)

        # Check if the square ends with the number
        return square_str.endswith(num_str)

# Get user input
number = int(input("Enter a positive integer: "))
# Create an instance of the Solution class
solution = Solution()
# Check if the number is automorphic and print the result
if solution.isAutomorphic(number):
    print(f"{number} is an automorphic number.")
else:
    print(f"{number} is not an automorphic number.")
