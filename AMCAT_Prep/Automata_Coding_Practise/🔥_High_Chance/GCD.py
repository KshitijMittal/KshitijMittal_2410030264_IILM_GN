'''
Greatest Common Divisor (GCD)

Theory: The Greatest Common Divisor (GCD), also known as Highest Common Factor (HCF), of two integers is the largest positive integer that divides both numbers without leaving a remainder. Euclid's algorithm states GCD(a,b) = GCD(b, a%b), terminating when b=0.

Problem: Given two positive integers a and b, return their Greatest Common Divisor (GCD).

Example 1:
Input: a = 48, b = 18
Output: 6
Explanation: GCD(48, 18) = 6 (divides both without remainder)

Example 2:
Input: a = 17, b = 13
Output: 1
Explanation: 17 and 13 are coprime (no common divisors except 1)

Constraints: 1 <= a, b <= 10^6
'''

class Solution:
    def gcd(self, a: int, b: int) -> int:
        # Implementing Euclid's algorithm for GCD
        while b:
            a, b = b, a % b  # Update a to b and b to the remainder of a divided by b
        return a  # When b becomes 0, a is the GCD

# Get user input
a = int(input("Enter the first positive integer: "))
b = int(input("Enter the second positive integer: "))
# Create an instance of the Solution class
solution = Solution()
# Find the GCD of the two integers and print the result
gcd_result = solution.gcd(a, b)
print(f"The Greatest Common Divisor of {a} and {b} is: {gcd_result}")
