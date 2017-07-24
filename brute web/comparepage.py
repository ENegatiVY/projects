import re
from bs4 import BeautifulSoup
#得到一个关键词字典，格式为{关键字：词频}
#page=
def find_keyword(page):
    searchdict={}
    # print(page)
    page=BeautifulSoup(page,'html5lib')
    taglist=[tag.name for tag in page.find_all()]
    # print(wordlist)
    for i in taglist:
        if i not in searchdict:
            searchdict[i]=1
        else:
            searchdict[i]+=1
    # print(searchdict)
    return  searchdict

def compare_dict(dictionary1,dictionary2):
    error=0
    for i in dictionary1:
        if i in dictionary2:
            error+=abs(dictionary2[i]-dictionary1[i])
            dictionary2[i]=0
        else:
            error+=dictionary1[i]
    for i in dictionary2:
        error+=dictionary2[i]
    # print(error)
    if error<3:
        error=1  #错误较少，认为是一个网页
    else:
        error=0  #错误较多，认为不是一个网页
    return error

def compare_page(page1,page2):
    dict1=find_keyword(page1)
    dict2=find_keyword(page2)
    # print(dict1,'\n',dict2)
    return compare_dict(dict1,dict2)
