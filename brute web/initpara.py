#这个程序是为了找到url里面需要提交的的参数

import re
import requests
from bs4 import BeautifulSoup
headers= {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36'
                           ' (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36'),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded'}

def is_login(url):
    session = requests.session()
    cont = session.get(url,headers=headers).content
    soup = BeautifulSoup(cont,"html5lib")
    pwd_list = soup.find_all('input',type='password')
    text_list = soup.find_all('input',type='text')
    if len(pwd_list) ==1 and len(text_list) != 0:
        return soup
    else:
        # raise ValueError('This page is not a login page')
        return soup

def get_post(url):
    soup=is_login(url)
    #这个地方是寻找post表单，但是这个方法只适用于php服务器
    post_form=[]
    post_form_low=soup.find_all('form',method='post')
    post_form_upp=soup.find_all('form',method='POST')
    #因为找不到的情况下
    if isinstance(post_form_low,list):
        post_form+=post_form_low
    if isinstance(post_form_upp,list):
        post_form+=post_form_upp
    # print(post_form)
    print(len(post_form))
    if len(post_form)!=1:
        raise ValueError('post form num error')
    return post_form


def get_post_xjtu(url):
    whether_login,soup=is_login(url)
    #这个地方是寻找post表单，但是这个方法只适用于php服务器
    postform=soup.find_all(attrs={'method':'post','method':'POST'})
    # print(postform)
    if len(postform)!=1:
        raise ValueError('post form num error')
    return postform

def init_para(url):
    #初始化一个字典，提交一些非账户和密码的数据，同时返回一个列表，字典第一项为用户名的标识，第二项为密码的标志
    postform=get_post(url)
    post_dict={}
    pass_name=[]
    input_list=postform[0].find_all('input')
    id_num=0
    name_num=0
    for tag in input_list:
        if tag.get('id'):
            id_num+=1
        if tag.get('name'):
            name_num+1
    if id_num > name_num:
        for tag in input_list:
            if tag.get('id')!=None:
                if tag.get('value')=='' and tag.get('type')=='password':
                    pass_name.append(tag.get('id'))
                if tag.get('value')=='' and tag.get('type')=='text':
                    pass_name.append(tag.get('id'))
                elif tag.get('value')!='':
                    post_dict[tag.get('id')]=tag.get('value') if tag.get('value')!=None else ''
    else:
        # print('mark')
        for tag in input_list:
            if tag.get('name')!=None:
                if tag.get('value')==('' or None) and tag.get('type')=='password':
                    pass_name.append(tag.get('name'))
                if tag.get('value')==('' or None) and tag.get('type')=='text':
                    pass_name.append(tag.get('name'))
                elif tag.get('value') != '':
                    post_dict[tag.get('name')] = tag.get('value') if tag.get('value')!=None else ''
    # print(post_dict,pass_name)
    return post_dict,pass_name

def init_postdata(url,username,password,para_dict,pass_name):
    #通过用户名和密码做一个字典作为postdata
    # para_dict,pass_name=init_para(url)
    #tmp for nicaifu.com
    postdata=para_dict
    postdata={}
    postdata['pin'] = password
    postdata['code'] = username
    postdata[pass_name[1]]=password
    postdata[pass_name[0]]=username
    return postdata


def init_wrongpage(url):
    para_dict,pass_name=init_para(url)
    wrong_postdata=init_postdata(url,'admin','123456',para_dict,pass_name)
    wrong_page=requests.post(url=url,headers=headers,data=wrong_postdata)
    return wrong_page



