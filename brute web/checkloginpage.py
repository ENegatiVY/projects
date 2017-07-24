
from bs4 import BeautifulSoup
import requests
def is_login(url):
    headers = {
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36'
                       ' (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36'),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded'}
    session = requests.session()
    cont = session.get(url,headers=headers).content
    soup = BeautifulSoup(cont,"html5lib")
    path =soup
    pwd_list = path.find_all('input',type='password')
    text_list = path.find_all('input',type='text')
    if len(pwd_list) ==1 and len(text_list) != 0:
        return True,soup
    else:
        return False,soup

# print(is_login('http://cy.xjtu.edu.cn/wp-login.php'))
