'''
Maximum of Three Numbers

Theory: Finding max of three numbers requires two comparisons: first find max of first two, then compare with third. Can use built-in max() or conditionals.

Problem: Given three integers a, b, c, return the largest among them.

Example 1:
Input: a = 1, b = 5, c = 3
Output: 5

Example 2:
Input: a = 10, b = 10, c = 10
Output: 10

Constraints: 0 <= a,b,c <= 10^9
'''

class Solution:
    def maxOfThree(self, a: int, b: int, c: int) -> int:
        # Using built-in max function to find the maximum of three numbers
        return max(a, b, c)

# Get user input
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))
# Create an instance of the Solution class
solution = Solution()
# Find the maximum of the three integers and print the result
max_result = solution.maxOfThree(a, b, c)
print(f"The maximum of the three numbers is: {max_result}")
