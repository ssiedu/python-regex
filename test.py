import re;

s="this is python and python is object oriented language and rest is easy";

res1=re.findall("[p-s]",s);
print(res1);

#d is for single digit and d+ for group of digits (one or more)

s="i have started this business on 22 nd 2190 and run it for 3 years."
res2=re.findall("\d",s);  #(same as) res2=re.findall("[0-9]",s);
print(res2);

s="i have started this business on 22 nd 2190 and run it for 3 years."
res3=re.findall("\d+",s);  #(same as) res2=re.findall("[0-9]",s);
print(res3);

