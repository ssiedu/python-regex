import re;
str="rajesh is the raja of ramgang and rarely a raja like him found";
pt=r"(raj|ram)\w*";

res=re.search(pt,str);
print(res);
print(res.start());
print(res.end());
print(res.span());
print(res.group());
