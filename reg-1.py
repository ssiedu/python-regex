import re;

str="manoj121, education3 is fun";
pt=r"^\w+";
   #r"^\w+"
res=re.findall(pt,str);
print(res);

"""
import re
xx = "guru99,education is fun"
r1 = re.findall(r"^\w+",xx)
print(r1)
"""