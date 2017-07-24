import argparse
import re
import time
from lib.person import Person

def email(string):
    if not re.match(r'^[\w\d.-_]+@[\w\d.-]+\.[\w]{2,8}$', string):
        raise ValueError(string)
    return string


def date(date_string):
    if not date_string:
        return None
    return time.strptime(date_string, '%Y-%m-%d')


def parser():
    parser=argparse.ArgumentParser()
    parser.add_argument('-n', '--name', dest='name', action='store',
                        help='real name of target', nargs='*', default=[])
    parser.add_argument('-u', '--username', dest='username', action='store',
                        help='usernames of target, English only', nargs='*', default=[])
    parser.add_argument('-q', '--qq', dest='qq', action='store',
                        help='QQ numbers of target', nargs='*', type=int, default=[])
    parser.add_argument('-e', '--email', dest='email', action='store',
                        help='email addresses of target', nargs='*', type=email, default=[])
    parser.add_argument('-m', '--mobile', dest='mobile', action='store',
                        help='mobile phone/phone numbers of target', nargs='*', type=int, default=[])
    parser.add_argument('-b', '--birthday', dest='birthday', action='store',
                        help='birthday of target, format: %%Y-%%m-%%d', type=date, default=None)
    parser.add_argument('-c', '--company', dest='company', nargs='*', action='store',
                        help='company / website domain of target', type=str, default=[])
    parser.add_argument('--with-dict', dest='with_dict', action='store_true',
                        help='generate passwords with weak password dictionary')
    parser.add_argument('-o', '--output', dest='output_file', action='store',
                        help='output result to a json file', type=argparse.FileType('w'))

    args = parser.parse_args()
    print(args)
    print(args.__dict__)
    if not any(args.__dict__.values()):
        parser.print_help()
        raise SystemExit

    person_list = []
    person_list.append(Person(information=args.__dict__))

    return (args, person_list)


def init_dict_fromfile(filename):
    dictionary={}
    file=open(filename,'r',encoding='utf-8')
    file_content=file.read()
    file.close()
    dictionary['name'] = re.findall('name:(.*)',file_content)[0].split(' ')
    dictionary['username'] = re.findall('username:(.*)', file_content)[0].split(' ')
    dictionary['qq'] = re.findall('qq:(.*)', file_content)[0].split(' ')
    dictionary['email'] = re.findall('email:(.*)', file_content)[0].split(' ')
    dictionary['mobile'] = re.findall('mobile:(.*)', file_content)[0].split(' ')
    birthday = re.findall('birthday:(.*)', file_content)[0].split(' ')
    dictionary['birthday'] = [time.strptime(birthday[0],'%Y-%m-%d')]
    dictionary['company'] = re.findall('company:(.*)', file_content)[0].split(' ')
    dictionary['with_dict']=False
    dictionary['output_file']=False
    for key in dictionary:
        if dictionary[key]==['']:
            dictionary[key]=[]
    print(dictionary)
    return dictionary
# if __name__=='__main__':
#     parser()
