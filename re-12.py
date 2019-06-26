import re;

"""
str = "This rain in Spain and This is superb That is so natural"
pt="^Th.*ral$"; 
res=re.findall(pt,str);
print(res);
"""

str="this is python and python is superb";

pt="pythoncode*";

res=re.findall(pt,str);
print(res);