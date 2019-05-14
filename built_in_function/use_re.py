"""
created by nzh
Date: 2019/5/13 6:17 PM
"""
import re

# re.split()
content = "Split string by the occurrences      of pattern.         If capturing parentheses are used in pattern, then the text of all groups in the pattern are also returned as part of the resulting list. If maxsplit is nonzero, at most maxsplit splits occur, and the remainder of the string is returned as the final element of the list."

result = re.split(r'[,.\s]\s*', content)
print(result)


# re.match(regex, string, flags)


