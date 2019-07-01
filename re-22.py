import re
string = '1Indore2Bhopal3Ujjain4Mumbai5Deli'
pattern = '\d+'
result = re.split(pattern, string,2) # 2 indicates maximum no of splits
print(result)
