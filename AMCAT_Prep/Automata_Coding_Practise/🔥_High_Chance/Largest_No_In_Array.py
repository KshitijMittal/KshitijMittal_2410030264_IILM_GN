'''
Largest Element in Array

Theory: Finding the maximum element in an array requires a single pass through all elements, comparing each with the current maximum value found so far.

Problem: Given an array of integers nums, return the largest (maximum) element in the array.

Example 1:
Input: nums = [3,1,4,1,5,9,2], n = 7
Output: 9

Example 2:
Input: nums = [10,20,30,10,30], n = 5
Output: 30

Constraints: 1 <= n <= 1000, 0 <= nums[i] <= 10^5
'''

class Solution:
    def findLargest(self, nums: list[int], n: int) -> int:
        # Initialize the largest element to the first element of the array
        largest = nums[0]

        # Iterate through the array to find the largest element
        for i in range(1, n):
            if nums[i] > largest:
                largest = nums[i]

        return largest

# Get user input
n = int(input("Enter the number of elements in the array: "))
nums = list(map(int, input("Enter the elements of the array separated by space: ").split()))
# Create an instance of the Solution class
solution = Solution()
# Find the largest element in the array and print the result
largest_element = solution.findLargest(nums, n)
print(f"The largest element in the array is: {largest_element}")
