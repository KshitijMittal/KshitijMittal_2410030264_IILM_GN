'''
Spiral Matrix Print

Theory: Spiral order traversal visits matrix elements starting from top-left, moving right→down→left→up, spiraling inward until all elements are covered.

Problem: Given a 2D matrix, return all elements in spiral order (clockwise starting from top-left).

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints: 1 <= matrix.length <= 20, 1 <= matrix[i].length <= 20
'''

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix:
            return []

        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Traverse from left to right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # Traverse from top to bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                # Traverse from right to left
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                # Traverse from bottom to top
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result

# Get user input for the matrix
def get_matrix_input():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []
    print("Enter the elements row-wise:")
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

# Example usage
if __name__ == "__main__":
    matrix = get_matrix_input()
    solution = Solution()
    spiral_order = solution.spiralOrder(matrix)
    print(f"The spiral order of the matrix is: {spiral_order}")
