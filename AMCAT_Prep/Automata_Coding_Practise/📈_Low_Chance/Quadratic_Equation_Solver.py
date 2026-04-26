'''
Quadratic Equation Solver

Theory: Quadratic equation ax² + bx + c = 0 has discriminant D = b²-4ac. Roots: [-b±√D]/(2a). Real roots if D≥0, complex if D<0.

Problem: Given coefficients a, b, c, return the roots as list of floats (or complex if needed).

Example 1:
Input: a=1, b=-3, c=2
Output: [1.0, 2.0]
Explanation: D=1, roots solve (x-1)(x-2)=0

Example 2:
Input: a=1, b=0, c=1
Output: [0j, 0j]
Explanation: D=-4, complex roots

Constraints: 0 <= |a,b,c| <= 1000, a != 0
'''

class Solution:
    def quadraticRoots(self, a: float, b: float, c: float) -> list[complex]:
        import cmath
        D = b**2 - 4*a*c
        root1 = (-b + cmath.sqrt(D)) / (2*a)
        root2 = (-b - cmath.sqrt(D)) / (2*a)
        return [root1, root2]

# Get user input
a = float(input("Enter coefficient a (non-zero): "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
# Create an instance of the Solution class
solution = Solution()
# Find the roots of the quadratic equation and print the result
roots = solution.quadraticRoots(a, b, c)
print(f"The roots of the equation {a}x² + {b}x + {c} = 0 are: {roots[0]} and {roots[1]}")
