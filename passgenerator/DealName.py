import re
name='LiuKong'
def mainprocess(name):
    Firstletter=re.findall('([A-Z])',name)
    namepart=re.findall('([A-Z][a-z]*)',name)
    print(Firstletter)
    print(namepart)
    lowernamepart=lowername(namepart)
    letterpart=CombineLetter(Firstletter)
    mainlist=[]
    print(letterpart)
    mainlist=lowernamepart+namepart+letterpart
    print(mainlist)
    mainlist.append(name.capitalize())
    mainlist.append(name.lower())
    mainlist.append(name)
    mainlist.append('admin')
    mainlist.append('root')
    print(mainlist)
    return mainlist
def CombineLetter(Firstletter):
    firstletter=[]
    #firstletter.append(Firstletter[0])
    newstr=''.join(Firstletter)
    firstletter.append(newstr)
    firstletter.append(newstr.capitalize())
    return firstletter
def lowername(namepart):
    lowernamepart=[]
    for i in namepart:
        lowernamepart.append(i.lower())
    print(lowernamepart)
    return lowernamepart
mainprocess(name)
