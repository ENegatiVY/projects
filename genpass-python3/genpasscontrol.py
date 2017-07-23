from cmdparser import parser
from lib.person import Person
from rules.initrules import init_rule_file
from rules.checkpassrule import pass_startwith_alpha,pass_within_length,pass_startwith_digit
import time
def cmdgenerator():
    testinfo=parser()
    newperson=Person(information=testinfo)
    tmplist=newperson.generate_password()
    print(tmplist)
    for i in tmplist:
        print(i)


def functiongenerator(dict_of_info):
    target=Person(information=dict_of_info)
    return target.generate_password()

#设定规则组成方法
init_rule_file(2,1,1)
def generate_help():
    print('Dictionay example:')
    print("testinfo={'name': ['小明'], 'username': ['XiaoMing'], 'qq': [22222222], 'email': ['xiaoming@163.com'], 'mobile': [122222222], 'birthday': [time.striptime('1111-11-11','%Y-%m-%d')], 'company': ['Netease','网易'], 'with_dict': False, 'output_file': None}")

def generate_pass(info_dict,target_file):
    passlist=functiongenerator(info_dict)
    passfile=open(target_file,'w')
    for i in passlist:
        if pass_within_length(i,6,16) and (pass_startwith_alpha(i) or pass_startwith_digit(i)):
            passfile.write(i)
            passfile.write('\n')
    passfile.close()

