import re;

pt1="\s";               #space
pt2="\S";               #anything other than space
pt3="\d";               #any digit
pt4="\D";               #any thing except digit
pt5="\w";               #any alpha numeric
pt6="\W";               #anything other than alpha-numeric
pt7=".";                #any char



mystr="abA4Bx yZ9x@#  cDA9# $33";

matcher=re.finditer(pt7,mystr);
for match in matcher:
    print(match.start(),"\t",match.group());
    