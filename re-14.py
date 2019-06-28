import re;
str="ab abc abcc abcc axc adc";
#ptr="abc+";#+ for 1 or more c
#ptr="abc*";#* for 0 or more
ptr="a.c";#any char between between a and c
res=re.findall(ptr,str);
print(res);