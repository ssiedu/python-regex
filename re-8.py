import re;
str="S.B.I. F.B.I. R.B.I. F.C.O. P.M.O. K.L.I."
ptr=".\..\.I\.";    #(any char one 1 2nd . 3rd any char 4th . 5th I and 6th . )
res=re.findall(ptr,str);
print(res);