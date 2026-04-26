'''
Decimal to Octal Converter

Theory: Octal (base-8) conversion uses repeated division by 8, collecting remainders (0-7) from bottom-up, similar to binary (base-2).

Problem: Given a decimal number, return its octal representation as string.

Example 1:
Input: num = 74
Output: "112"
Explanation: 74 = 1×8² + 1×8¹ + 2×8⁰

Example 2:
Input: num = 10
Output: "12"

Constraints: 0 <= num <= 10^9
'''

class Solution:
    def decimalToOctal(self, num: int) -> str:
        if num == 0:
            return "0"

        octal = ''
        while num > 0:
            remainder = num % 8  # Get the remainder when divided by 8
            octal = str(remainder) + octal  # Prepend the remainder to the octal string
            num //= 8  # Update num by dividing it by 8

        return octal

# Get user input
decimal_input = int(input("Enter a decimal number: "))
# Create an instance of the Solution class
solution = Solution()
# Convert the decimal number to octal and print the result
octal_output = solution.decimalToOctal(decimal_input)
print(f"The octal representation of the decimal number {decimal_input} is: {octal_output}")
