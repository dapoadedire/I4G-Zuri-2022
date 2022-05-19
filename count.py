import re
line = "Okay, you are good to go"

count = len(re.findall(r"\w+", line))
print(count)