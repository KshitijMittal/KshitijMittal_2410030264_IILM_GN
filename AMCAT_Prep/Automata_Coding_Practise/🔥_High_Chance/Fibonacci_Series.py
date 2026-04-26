'''
Fibonacci Series Generator

Theory: The Fibonacci sequence is defined as F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2) for n>1. Each number is the sum of the two preceding ones: 0, 1, 1, 2, 3, 5, 8, 13, 21...

Problem: Return the Fibonacci series up to n terms (0-indexed).

Example 1:
Input: n = 6
Output: [0,1,1,2,3,5]

Example 2:
Input: n = 10
Output: [0,1,1,2,3,5,8,13,21,34]

Constraints: 0 <= n <= 30
'''

class Solution:
    def fibonacciSeries(self, n: int) -> list[int]:
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]

        series = [0, 1]
        for i in range(2, n + 1):
            next_term = series[i - 1] + series[i - 2]
            series.append(next_term)

        return series

# Get user input
n = int(input("Enter the number of terms in the Fibonacci series: "))
# Create an instance of the Solution class
solution = Solution()
# Generate the Fibonacci series and print the result
fibonacci_series = solution.fibonacciSeries(n)
print(f"The Fibonacci series up to {n} terms is: {fibonacci_series}")
