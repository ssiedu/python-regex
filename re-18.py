import re;
str="rajesh is ram the raja of ramgang and rarely a raja like him found";
pt=r"(raj|ram)\w?";     #   *(0 or more), +(1 or more), ?(0 or 1)

itr=re.finditer(pt,str);

for item in itr:
    print(item);
