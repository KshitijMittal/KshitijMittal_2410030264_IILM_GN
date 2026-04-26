'''
Maximum Sum Subarray

Theory: Kadane's algorithm finds maximum sum contiguous subarray by tracking current sum and resetting when negative. O(n) time solution.

Problem: Given an array of integers, return the maximum sum of any contiguous subarray.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has maximum sum 6

Example 2:
Input: nums = [1]
Output: 1

Constraints: 1 <= nums.length <= 10^5, -10^4 <= nums[i] <= 10^4
'''

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = float('-inf')  # Initialize max_sum to the smallest possible value
        current_sum = 0  # Initialize current_sum to 0

        for num in nums:
            current_sum += num  # Add the current number to current_sum
            max_sum = max(max_sum, current_sum)  # Update max_sum if current_sum is greater
            if current_sum < 0:  # If current_sum becomes negative, reset it to 0
                current_sum = 0

        return max_sum

# Get user input
n = int(input("Enter the number of elements in the array: "))
nums = list(map(int, input("Enter the elements of the array separated by space: ").split()))
# Create an instance of the Solution class
solution = Solution()
# Find the maximum sum of any contiguous subarray and print the result
max_sum_subarray = solution.maxSubArray(nums)
print(f"The maximum sum of any contiguous subarray is: {max_sum_subarray}")
