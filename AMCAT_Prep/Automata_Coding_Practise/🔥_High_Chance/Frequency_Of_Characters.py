'''
Character Frequency Counter

Theory: Character frequency maps each unique char to its count. Use dictionary/hashmap, iterate string once O(n) time.

Problem: Given a string s, return a dictionary mapping each character to its frequency.

Example 1:
Input: s = "hello"
Output: {"h":1, "e":1, "l":2, "o":1}

Example 2:
Input: s = "aabbcc"
Output: {"a":2, "b":2, "c":2}

Constraints: 1 <= s.length <= 10^5, lowercase English letters
'''

class Solution:
    def charFrequency(self, s: str) -> dict[str, int]:
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        return freq


# Get user input
input_string = input("Enter a string: ")
# Create an instance of the Solution class
solution = Solution()
# Get the character frequency and print the result
frequency = solution.charFrequency(input_string)
print(frequency)
