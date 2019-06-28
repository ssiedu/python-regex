import re;
str="rajesh is the raja of ramgang and rarely a raja like him found";
pt=r"(raj|ram)\w*";

res=re.sub(pt,str,"xyz");

print(str);
print(res);