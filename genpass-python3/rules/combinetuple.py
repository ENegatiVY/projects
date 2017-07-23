#这个程序的主要是为了将两个倍itertools处理后的tuple组合起来
def tupletransfer(itertooltype):
    tmptuple=()
    for j in itertooltype:
        #print(j)
        tmptuple+=j
    return tmptuple

def combinetupletogether(tuple1,tuple2):
    tmptuple=tuple2+tuple1
    return tmptuple

def addinlist(listforall,tmplist):
    return listforall+tmplist

def listtransfer(itertooltype):
    tmplist=[]
    for i in itertooltype:
        tmplist.append(i)
    return tmplist
def changetuple(i):
    tmpstr=''
    for j in i:
        tmpstr+=j
    return tmpstr