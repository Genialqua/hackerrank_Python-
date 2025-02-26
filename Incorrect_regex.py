import re

def isRegex(s):
    try:
        re.compile(s)
        return True
    except re.error:
        return False

# Number of test cases
n = int(raw_input())  # For Python 2.7, use raw_input()

# Loop through each pattern and test
for _ in range(n):
    pattern = raw_input().strip()  # Get pattern from input
    print("True" if isRegex(pattern) else "False")