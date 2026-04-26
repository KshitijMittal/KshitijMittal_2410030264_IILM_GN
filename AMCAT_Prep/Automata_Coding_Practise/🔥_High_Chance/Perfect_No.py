'''
Perfect Number Check

Theory: A perfect number is a positive integer equal to the sum of its proper divisors (excluding the number itself). The first perfect number is 6 (1+2+3=6), and the second is 28 (1+2+4+7+14=28).

Problem: Return true if num is a perfect number, where a perfect number is a positive integer equal to the sum of its proper divisors.

Example 1:
Input: num = 28
Output: true
Explanation: 1 + 2 + 4 + 7 + 14 = 28

Example 2:
Input: num = 27
Output: false

Constraints: 1 <= num <= 10^7
'''

class Solution:
    def isPerfect(self, num: int) -> bool:
        if num < 2:
            return False  # Perfect numbers are greater than 1

        # Calculate the sum of proper divisors
        divisor_sum = 1  # Start with 1, which is a proper divisor
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:  # If i is a divisor
                divisor_sum += i
                if i != num // i:  # Add the complementary divisor if it's different
                    divisor_sum += num // i

        return divisor_sum == num

# Get user input
number = int(input("Enter a positive integer: "))
# Create an instance of the Solution class
solution = Solution()
# Check if the number is a perfect number and print the result
if solution.isPerfect(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
