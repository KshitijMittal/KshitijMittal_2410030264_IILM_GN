'''
Binary to Octal Converter

Theory: Binary to octal groups 3 binary digits per octal digit (8=2^3). Pad with leading zeros if needed, convert each group: 000=0, 001=1, ..., 111=7.

Problem: Given a binary string, return its octal representation.

Example 1:
Input: binary = "1101010"
Output: "152"
Explanation: 110-101-010 → 6-5-2

Example 2:
Input: binary = "1111"
Output: "17"

Constraints: binary length 1-32, valid binary digits
'''

class Solution:
    def binaryToOctal(self, binary: str) -> str:
        # Pad the binary string with leading zeros to make its length a multiple of 3
        while len(binary) % 3 != 0:
            binary = '0' + binary

        octal = ''
        # Process each group of 3 bits
        for i in range(0, len(binary), 3):
            group = binary[i:i+3]  # Get the current group of 3 bits
            octal_digit = str(int(group, 2))  # Convert the group from binary to decimal and then to string
            octal += octal_digit  # Append the octal digit to the result

        return octal

# Get user input
binary_input = input("Enter a binary string: ")
# Create an instance of the Solution class
solution = Solution()
# Convert the binary string to octal and print the result
octal_output = solution.binaryToOctal(binary_input)
print(f"The octal representation of the binary string {binary_input} is: {octal_output}")
