
import re
day='2001.11.21'

def mainprocess(day):
    mainlist=[]
    part=re.findall('([0-9]*)',day)
    print(part)
    mainlist.append(''.join(part))
    mainlist.append(''.join(part)[2:])
    print(part[2]+part[4])
    mainlist.append(part[2]+part[4])
    yearlist=dealyear(part[0])
    mainlist+=yearlist

    print(mainlist)
    return mainlist
def dealyear(str):
    yearlist=[]
    yearlist.append(str)
    pureyear=str[2:]
    yearlist.append(pureyear)
    return yearlist
