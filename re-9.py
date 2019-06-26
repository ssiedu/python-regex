import re;
str="this is my string and we are searching for ab9 string xy34";

ptr1="[a-z]{3,5}";#pattern for searching any string of length 3 to 5 chars
res1=re.findall(ptr1,str);
print(res1);

ptr2="\w{3,5}";#pattern for searching any alphanumeric string of length 3-5
res2=re.findall(ptr2,str);
print(res2);