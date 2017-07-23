from .combinetuple import tupletransfer,combinetupletogether,addinlist,listtransfer,changetuple
from itertools import permutations,combinations
# from .chackpassrule import pass_startwithalpha,pass_within_length
from .constfile import infoList,charList,constantList
import os
#第一组里面可能有一个或两个元素
#第二组里面可能有零个或一个元素
#第三组里面可能有零个或一个元素
pathstart=os.path.dirname(__file__)
print(pathstart)
def generate_rule(info,info_maxnum,char,char_maxnum,const,const_maxnum):
    all_rule_list=[]
    for i in range(1,info_maxnum+1):
        for j in range(0,char_maxnum+1):
            for k in range(0,const_maxnum+1):
                # print(i,j,k)
                info_list = combinations(info, i)
                for o in info_list:
                    info_element=listtransfer(o)
                    char_list = combinations(char, j)
                    for p in char_list:
                        char_element=listtransfer(p)
                        const_list=combinations(const,k)
                        for q in const_list:
                            const_element=listtransfer(q)
                            all_element=info_element+char_element+const_element
                            rule_list=listtransfer(permutations(all_element,i+j+k))
                            all_rule_list+=rule_list
    return all_rule_list
# rulelist=generate_rule(infoList,2,charList,1,constantList,1)

def init_rule_file(info_maxnum,char_maxnum,const_maxnum):
    rulefile=open(pathstart+'\combinations.py','w')
    rulelist=generate_rule(infoList,info_maxnum,charList,char_maxnum,constantList,const_maxnum)
    rulefile.write('rules = [\n')
    for i in rulelist:
        string=changetuple(i)
        rulefile.write('\''+string+'\',\n')
    rulefile.write(']')
    rulefile.close()

# initfile(2,1,1)
