import re;
str="3435 868685 89889 688668 848495 898897987 87899 22 454454"
pt1="\s\d{5}\s";#pattern for checking 5 digit number
pt2="\d{5,7}";#pattern for checking 5-7 digit number
#res=re.findall(pt1,str);
res=re.findall(pt2,str);
print(res);