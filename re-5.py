import re;

str="rat cat mat fat";

res=re.findall("[^rc]at",str);   #searching for any string having first char other than r or c and "at" on 2 and 3 pos

print(res);

