'''
Armstrong Numbers in Range

Theory: Armstrong numbers equal the sum of their digits raised to power of digit count. Range finding requires checking each number in interval.

Problem: Return all Armstrong numbers between low and high (inclusive).

Example 1:
Input: low = 1, high = 1000
Output: [1,153,370,371,407]

Example 2:
Input: low = 10000, high = 20000
Output: []

Constraints: 0 <= low <= high <= 10^9
'''

class Solution:
    def armstrongRange(self, low: int, high: int) -> list[int]:
        armstrong_numbers = []
        for num in range(low, high + 1):
            num_str = str(num)
            n = len(num_str)
            armstrong_sum = sum(int(digit) ** n for digit in num_str)
            if armstrong_sum == num:
                armstrong_numbers.append(num)
        return armstrong_numbers

# Get user input
low = int(input("Enter the lower bound of the range: "))
high = int(input("Enter the upper bound of the range: "))
# Create an instance of the Solution class
solution = Solution()
# Get the Armstrong numbers in the range and print the result
armstrong_numbers = solution.armstrongRange(low, high)
print(f"Armstrong numbers in the range [{low}, {high}] are: {armstrong_numbers}")
