'''
Palindrome Pattern Printer

Theory: Palindrome patterns read same forwards/backwards per row/line, often increasing to middle then mirroring (like diamond but palindromic rows).

Problem: Print a palindrome number pattern of height n (row i: 1 to i to 1).

Example 1:
Input: n = 4
Output:
1
212
32123
4321234

Constraints: 1 <= n <= 20
'''

class Solution:
    def printPalindromePattern(self, n: int) -> None:
        for i in range(1, n + 1):
            # Create the left part of the palindrome (descending)
            left_part = ''.join(str(x) for x in range(i, 0, -1))
            # Create the right part of the palindrome (ascending, excluding the middle element)
            right_part = ''.join(str(x) for x in range(2, i + 1))
            # Combine both parts to form the full palindrome pattern for the current row
            print(left_part + right_part)

# Example usage:
if __name__ == "__main__":
    n = 4
    solution = Solution()
    solution.printPalindromePattern(n)
# Output:
# 1
# 212
# 32123
# 4321234