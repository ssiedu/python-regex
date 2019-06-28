import re;

f=open("data.txt");
res=f.read();
#print(res);

#pt1=r"\b\d\d\d\d-\d\d\d\d\d\d";
#pt1=r"\b\d{5}.\d{5,6}\b";#will take . and - both (here . is for any character)
#pt1=r"\b\d{5}\.\d{5,6}\b";#will take . only (searching for . only)
pt1=r"\b\d{5}.\d{5,6}\b"
pt1=r"\b07\d{3}.\d{5,6}\b";#07 and then 3 digits and then 5-6 digits
pt1=r"\b07\d{2,3}.\d{5,6}\b";#07 and then 2-3 digits and then 5-6 digits
res=re.findall(pt1,res);
print(res);