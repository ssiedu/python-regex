import re;

str="this is java and java is object oriented";

pattern=re.compile("java");

res=pattern.sub("oracle",str);  #replacing java with oracle

print(str);
print(res);