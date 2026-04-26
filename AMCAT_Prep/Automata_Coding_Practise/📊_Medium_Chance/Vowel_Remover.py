'''
Vowel Remover

Theory: Vowels are a,e,i,o,u (case-insensitive). Removing them scans string, collecting/skiping consonants, rebuilding result.

Problem: Given a string s, return the string with all vowels removed.

Example 1:
Input: s = "hello world"
Output: "hll wrld"

Example 2:
Input: s = "aeiou"
Output: ""

Constraints: 1 <= s.length <= 10^5, lowercase English letters
'''

class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        result = []
        for char in s:
            if char not in vowels:
                result.append(char)
        return ''.join(result)

# Example usage:
solution = Solution()
print(solution.removeVowels("hello world"))  # Output: "hll wrld"
print(solution.removeVowels("aeiou"))        # Output: ""
# Get user input
input_string = input("Enter a string: ")
# Remove vowels from the input string and print the result
result = solution.removeVowels(input_string)
print(f"The string with vowels removed is: {result}")
