import re

# Using re.match() to check if the string starts with "Python"
text = "Python is amazing"
result = re.match("Python", text)

if result:
    print("Match found:", result.group())
else:
    print("No match")           # Output: Match found: Python


# Using re.search() to find "Python" anywhere in the string
text = "I am learning Python"
result = re.search("Python", text)
print(result.group())           # Output: Python


# Using re.findall() to find all occurrences of "ai" in the string
text = "The rain in Spain falls mainly on the plain"
matches = re.findall("ai", text)
print(matches)                  # Output: ['ai', 'ai', 'ai', 'ai']


# Using re.sub() to replace all digits with "X"
text = "Agent 007 and Agent 999"
# Replace digits with X
new_text = re.sub(r"\d", "X", text)
print(new_text)                 # Output: Agent XXX and Agent XX


# Using re.split() to split a string by multiple delimiters
text = "apple,banana;cherry orange"
# Split by comma, semicolon, or space
fruits = re.split(r"[,;\s]", text)
print(fruits)                   # Output: ['apple', 'banana', 'cherry', 'orange']


# Using re.group() to extract specific parts of a match
text = "John Smith"
pattern = r"(\w+) (\w+)"
match = re.search(pattern, text)
print(match.group(0)) # John Smith (Entire match)
print(match.group(1)) # John (First group)
print(match.group(2)) # Smith (Second group)


# Using non-capturing groups to match a pattern without storing it as a group
pattern = r"(?:Mr|Ms|Dr)\. \w+"
text = "Mr. Bond"
# The title is matched but not stored as a separate group 1.


# Using named groups to give a name to the captured groups
pattern = r"(?P\w+) (?P\w+)"
match = re.search(pattern, "Jane Doe")
print(match.group('first')) # Jane
print(match.group('last'))  # Doe


# Using backreferences to match a repeated word
pattern = r"(\b\w+)\s+\1"
text = "This is the the end"
match = re.search(pattern, text)
print(match.group()) # "the the"