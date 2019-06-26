import re;
#searching for group of things
pattern1="[abc]";#either a or  b or c
pattern2="[^abc]";#anything except a,b or c
pattern3="[a-z]";#any lowercase symbol
pattern4="[A-Z]";#any uppercase symbol
pattern5="[a-zA-Z]";#any alphabates symbol
pattern6="[0-9]";#any digit
pattern7="[a-zA-Z0-9]"#any alpha-numeric character
pattern8="[^a-zA-Z0-9]"#anything otherthan digit or alphabate
#^ starts with
#$ ends with
mystr="abA4BxyZ9x@#cDA9#$33";

matcher=re.finditer(pattern8,mystr);
for match in matcher:
    print(match.start(),"\t",match.group());
    