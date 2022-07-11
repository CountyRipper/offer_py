n = input()
strs=[]
import re
def regexcheck(str):
    return re.match(r'^([a-zA-Z])([a-zA-z]*)([0-9]+)+([a-zA-Z0-9]*)$',str)
def check(str):
    num=False
    if len(str)>20 or len(str)<=1:
        return False
    if not((str[0]>='A'and str[0]<='Z')or(str[0]>='a' and str[0]<='z')):
        return False
    for i in str:
        if (i>='a'and i<='z')or (i>='A' and i<='Z' ):
            continue;
        if (i>='0' and i<='9'):
            num=True
        else:
            return False
    return num
for i in range(int(n)):
    strs.append(input())
for i in strs:
    if regexcheck(i):
        print("Accept")
    else:
        print("Wrong")
