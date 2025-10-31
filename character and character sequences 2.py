# CHARACTER AND CHARACTER SEQUENCES 2

# * - Repeats a character zero or more times.
# + - Repeats a character one or more times.
# ? - Matches zero or one occurrence of a character.
# ( - Indicates where string extraction to starts.
# ) - Indicates where string extraction to ends.

import re
string = "Hello World @ 123"
pattern = "\d*"  # Matches one or more digits
print(re.findall(pattern, string))  # Finds all occurrences of one or more digits in the string