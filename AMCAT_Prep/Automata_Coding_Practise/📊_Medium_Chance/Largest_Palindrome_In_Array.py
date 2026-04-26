'''
Largest Palindrome in Array

Theory: Palindrome numbers read same forwards/backwards. Find max among array elements that are palindromes.

Problem: Given an array of integers, return the largest palindrome number, or -1 if none exists.

Example 1:
Input: nums = [1221, 123, 343, 1001]
Output: 1221

Example 2:
Input: nums = [123, 456]
Output: -1

Constraints: 1 <= nums.length <= 10^5, 0 <= nums[i] <= 10^9
'''

class Solution:
    def largestPalindrome(self, nums: list[int]) -> int:
        def is_palindrome(num: int) -> bool:
            num_str = str(num)
            return num_str == num_str[::-1]

        largest_palindrome = -1
        for num in nums:
            if is_palindrome(num) and num > largest_palindrome:
                largest_palindrome = num

        return largest_palindrome

# Get user input
n = int(input("Enter the number of elements in the array: "))
nums = list(map(int, input("Enter the elements of the array separated by space: ").split()))
# Create an instance of the Solution class
solution = Solution()
# Find the largest palindrome in the array and print the result
largest_palindrome = solution.largestPalindrome(nums)
if largest_palindrome != -1:
    print(f"The largest palindrome in the array is: {largest_palindrome}")
else:
    print("No palindrome number found in the array.")
