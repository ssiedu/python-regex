import re;
str="ramesh suresh dinesh mahesh rajesh amita sumit pramesh raja";
pt1=".a";   #pattern for searching strings having a on send pos (. means any single char)
res=re.findall(pt1,str);
print(res);
