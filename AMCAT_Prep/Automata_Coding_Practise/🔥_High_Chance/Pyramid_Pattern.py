'''
Pyramid Pattern Printer

Theory: Pyramid patterns print numbers/symbols in triangular form, increasing then decreasing per row. Common in programming interviews to test nested loops and pattern logic.

Problem: Print a pyramid pattern of height n using numbers (row i contains i repeated i times).

Example 1:
Input: n = 4
Output:
   1
  22
 333
4444

Constraints: 1 <= n <= 20
'''

class Solution:
    def printPyramid(self, n: int) -> None:
        for i in range(1, n + 1):
            # Print spaces for left padding
            print(' ' * (n - i), end='')
            # Print the number i, repeated i times
            print(str(i) * i)

# Get user input
n = int(input("Enter the height of the pyramid: "))
# Create an instance of the Solution class
solution = Solution()
# Print the pyramid pattern
solution.printPyramid(n)
