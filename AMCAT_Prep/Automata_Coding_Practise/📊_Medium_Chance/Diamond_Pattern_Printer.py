'''
Diamond Pattern Printer

Theory: Diamond patterns form diamond shape: upper triangle increasing, lower decreasing symmetrically. Uses nested loops for spacing/numbers.

Problem: Print a diamond pattern of height 2n-1 centered with numbers/symbols.

Example 1:
Input: n = 3
Output:
  *
 ***
*****
 ***
  *

Constraints: 1 <= n <= 20
'''

class Solution:
    def printDiamond(self, n: int) -> None:
        # print diamond of diameter 2n-1
        for i in range(1, n + 1):
            # Print spaces for left padding
            print(' ' * (n - i), end='')
            # Print the number i, repeated (2*i - 1) times
            print(str(i) * (2 * i - 1))
        for i in range(n - 1, 0, -1):
            # Print spaces for left padding
            print(' ' * (n - i), end='')
            # Print the number i, repeated (2*i - 1) times
            print(str(i) * (2 * i - 1))

# Get user input
n = int(input("Enter the height of the diamond (n): "))
# Create an instance of the Solution class
solution = Solution()
# Print the diamond pattern
solution.printDiamond(n)
