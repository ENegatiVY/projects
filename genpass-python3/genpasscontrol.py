from cmdparser import parser,init_dict_fromfile
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
    return target.generate_username(),target.generate_password()


def generate_help():
    print('Dictionay example:')
    print("testinfo={'name': ['小明'], 'username': ['XiaoMing'], 'qq': [22222222], 'email': ['xiaoming@163.com'], 'mobile': [122222222], 'birthday': [time.striptime('1111-11-11','%Y-%m-%d')], 'company': ['Netease','网易'], 'with_dict': False, 'output_file': None}")

def generate_pass(info_dict,target_user_file,target_pass_file):
    user_list,pass_list=functiongenerator(info_dict)
    passfile=open(target_pass_file,'w')
    for i in pass_list:
        if pass_within_length(i,6,16) and (pass_startwith_alpha(i) or pass_startwith_digit(i)):
            passfile.write(i)
            passfile.write('\n')
    passfile.close()
    userfile=open(target_user_file,'w')
    for i in user_list:
        userfile.write(i)
        userfile.write('\n')
    userfile.close()

#设定规则组成方法
# init_rule_file(2,0,1)
filename='info.txt'
user_info=init_dict_fromfile(filename)
generate_pass(user_info,'user.txt','pass.txt')