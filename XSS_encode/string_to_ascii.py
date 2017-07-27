#网上虽然有一些在线的编码转换程序，但是却只是纯转换，无法输出我想要的格式，使用不方便，故写此程序
import re
import binascii

def select_mode(string,header):
    if string=='quit':
        exit('quit')
    elif string=='1':
        transfer_to_ascii(header)
    elif string=='2':
        transfer_to_hex()
    elif re.findall('^set',string):
        header[0]=re.findall('^set (.*)',string)[0]
        print("you have set header to :",header)
    else:
        help_func()
        return

def help_func():
    print('input 1 to transfer character to ascii')
    print('input 2 to transfer character to hex')
    print('use \'set\'+\'special string\' to change the special string\nexample:\'set &\' ')
    print('input quit to quit')
    return

def transfer_to_ascii(header):
    while True:
        print('You can input \'quit\' to go back to the main menu')
        raw_string=input("please input the string to transfer to ascii: ")
        tranfer_string=''
        if raw_string=='quit':
            return
        for i in raw_string:
            tranfer_string=tranfer_string+header[0]+str(ord(i))
        print(tranfer_string)

def transfer_to_hex():
    while True:
        print('You can input \'quit\' to go back to the main menu')
        raw_string=input("please input the string to transfer to hex: ")
        tranfer_string=''
        if raw_string=='quit':
            return
        for i in raw_string:
            tranfer_string=tranfer_string+str(hex(ord(i)))
        print(tranfer_string)

def main():
    help_func()
    header=['']
    header[0]=['&#']
    while True:
        raw_string=input('Please select your mode or set the header')
        select_mode(raw_string,header)
        print(header)



if __name__ == '__main__':
    main()