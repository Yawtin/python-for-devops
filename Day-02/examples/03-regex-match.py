import re

text = "The quick brown fox"
pattern = "quick"

match = re.match(pattern, text) //match function only searches at the start of the string, so the output is false
if match:
    print("Match found:", match.group())
else:
    print("No match")
