'''
Binary-Decimal Converter

Theory: Binary to decimal uses positional notation (rightmost=2^0). Decimal to binary uses repeated division by 2, collecting remainders bottom-up.

Problem: Given a decimal number, return its binary representation as string. Given binary string, return decimal value.

Example 1:
Input: num = 10
Output: "1010"

Example 2:
Input: binary = "1010"
Output: 10

Constraints: 0 <= num <= 10^9, binary length <= 32
'''

class Solution:
    def binaryDecimalConvert(self, num: int, isDecimalToBinary: bool) -> str:
        if isDecimalToBinary:
            if num == 0:
                return "0"
            binary = ''
            while num > 0:
                remainder = num % 2
                binary = str(remainder) + binary
                num //= 2
            return binary
        else:
            return str(int(num, 2))

# Get user input
choice = input("Choose conversion: 1 for Decimal to Binary, 2 for Binary to Decimal: ")
solution = Solution()
if choice == '1':
    decimal_input = int(input("Enter a decimal number: "))
    binary_output = solution.binaryDecimalConvert(decimal_input, True)
    print(f"The binary representation of the decimal number {decimal_input} is: {binary_output}")
elif choice == '2':
    binary_input = input("Enter a binary string: ")
    decimal_output = solution.binaryDecimalConvert(binary_input, False)
    print(f"The decimal representation of the binary string {binary_input} is: {decimal_output}")
else:
    print("Invalid choice. Please choose 1 or 2.")
