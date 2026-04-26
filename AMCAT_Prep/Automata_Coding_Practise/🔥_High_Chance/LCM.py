'''
Least Common Multiple

Theory: The Least Common Multiple (LCM) of two integers a and b is the smallest positive integer divisible by both a and b. LCM can be computed using GCD: LCM(a,b) = (a × b) / GCD(a,b).

Problem: Given two positive integers a and b, return their Least Common Multiple (LCM).

Example 1:
Input: a = 3, b = 6
Output: 6
Explanation: LCM(3, 6) = 6

Example 2:
Input: a = 4, b = 6
Output: 12

Constraints: 1 <= a, b <= 10^6
'''

class Solution:
    def findLargest(self, nums: list[int], n: int) -> int:
        # Function to calculate GCD using Euclidean algorithm
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        # Calculate GCD of a and b
        common_divisor = gcd(a, b)

        # Calculate LCM using the relationship between GCD and LCM
        lcm = (a * b) // common_divisor

        return lcm

# Get user input
a = int(input("Enter the first positive integer: "))
b = int(input("Enter the second positive integer: "))
# Create an instance of the Solution class
solution = Solution()
# Find the LCM of the two integers and print the result
lcm_result = solution.findLargest(a, b)
print(f"The Least Common Multiple of {a} and {b} is: {lcm_result}")
