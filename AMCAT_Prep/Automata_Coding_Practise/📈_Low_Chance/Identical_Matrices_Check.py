'''
Identical Matrices Check

Theory: Two matrices are identical if they have same dimensions and corresponding elements are equal. Requires row-col iteration with bounds checking.

Problem: Given two 2D matrices, return true if they are identical (same dimensions and elements).

Example 1:
Input: matrix1 = [[1,2],[3,4]], matrix2 = [[1,2],[3,4]]
Output: true

Example 2:
Input: matrix1 = [[1,2],[3,4]], matrix2 = [[1,3],[3,4]]
Output: false

Constraints: 1 <= matrix.length <= 50, 1 <= matrix[i].length <= 50
'''

class Solution:
    def areIdentical(self, matrix1: list[list[int]], matrix2: list[list[int]]) -> bool:
        # Check if dimensions are the same
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            return False

        # Compare each element
        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                if matrix1[i][j] != matrix2[i][j]:
                    return False

        return True  # All elements are identical


# Get user input for two matrices
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
    print("Enter details for the first matrix:")
    matrix1 = get_matrix_input()

    print("Enter details for the second matrix:")
    matrix2 = get_matrix_input()

    solution = Solution()
    result = solution.areIdentical(matrix1, matrix2)
    print(f"The matrices are {'identical' if result else 'not identical'}")
