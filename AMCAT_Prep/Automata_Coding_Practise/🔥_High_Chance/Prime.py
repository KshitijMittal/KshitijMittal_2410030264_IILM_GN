'''
Prime Number Check

Theory: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The first few primes are 2, 3, 5, 7, 11, 13, etc.

Problem: Given a positive integer num, return true if it is prime (has no divisors other than 1 and itself).

Example 1:
Input: num = 17
Output: true
Explanation: 17 is prime

Example 2:
Input: num = 15
Output: false
Explanation: 15 is divisible by 3 and 5

Constraints: 2 <= num <= 10^7
'''

class Solution:
    def isPrime(self, num: int) -> bool:
        if num <= 1:
            return False  # 0 and 1 are not prime numbers
        if num <= 3:
            return True   # 2 and 3 are prime numbers

        # Check for factors from 2 to the square root of num
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:  # If num is divisible by any number other than 1 and itself
                return False

        return True  # If no divisors found, num is prime

# Get user input
number = int(input("Enter a positive integer: "))
# Create an instance of the Solution class
solution = Solution()
# Check if the number is prime and print the result
if solution.isPrime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
