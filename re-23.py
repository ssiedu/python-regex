import re
# multiline string
string="""
    this is python and
    python is object oriented
    python is powerful
"""
# matches all whitespace characters
#pattern = '\s+'
#pattern="\n";
# empty string
#replace = '\t'
pattern="python";
replace="java";
new_string = re.sub(pattern, replace, string) #replacing all new line with tab space
print(string);
print("_"*100);
print(new_string)