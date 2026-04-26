'''
Prime Numbers in Range

Theory: Prime numbers greater than 1 have no divisors other than 1 and themselves. Efficient range checking uses Sieve of Eratosthenes or trial division up to sqrt(n).

Problem: Return all prime numbers in the range [1, n] inclusive.

Example 1:
Input: n = 10
Output: [2,3,5,7]

Example 2:
Input: n = 20
Output: [2,3,5,7,11,13,17,19]

Constraints: 1 <= n <= 10^5
'''

class Solution:
    def primesInRange(self, n: int) -> list[int]:
        if n < 2:
            return []  # No primes less than 2

        primes = []
        for num in range(2, n + 1):
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)

        return primes

# Get user input
n = int(input("Enter a positive integer: "))
# Create an instance of the Solution class
solution = Solution()
# Get the prime numbers in the range and print the result
prime_numbers = solution.primesInRange(n)
print(f"Prime numbers in the range [1, {n}] are: {prime_numbers}")
