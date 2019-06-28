import re;
str="rajesh is the raja of ramgang and rarely a raja like him found";
pt=r"(raj|ram)\w*";

"""
str='''
Mr. Raja
Ms. Rashmi
Mrs. Rita
Mr. Amit
Mrs. riya
''';
"""
#pt=r"(Mr|Ms|Mrs)\.?\s[A-Z]\w*";

#res=re.findall(pt,str);
#print(res);
itr=re.finditer(pt,str);
for item in itr:
    print(item);