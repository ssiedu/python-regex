import re;

str="this is java and java is object oriented javajobs are easily available";

pattern1=re.compile("\s\w{4}\s");
pattern2=" HELLO ";
res=pattern1.sub(pattern2,str);  #replacing any 4 alpha-numeric string with HELLO

print(str);
print(res);