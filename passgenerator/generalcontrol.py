#此程序是基于社会工程学方法生成一个小型爆破字典
#需要收集的信息是用户的姓名（全拼），还有生日

#处理姓名的程序，主要目的是将全拼'XiaoMing'姓名变为一个与姓名有关的列表，之后组合的时候从表中选取元素
Name='XiaoMing'
import DealName
Namelist=DealName.mainprocess(Name)
#print(Namelist)
#处理生日的程序，主要是将字符串生日划分为有意义的列表，输入格式为'1999.99.99'


birthday='2002.2.22'
import DealBirthday
Birthdaylist=DealBirthday.mainprocess(birthday)
#print(Birthdaylist)



#导入特殊字符列表
import DealChar
charlist=DealChar.returncharlist()
#print(charlist)
passfile=open(Name+'pass.txt','w')
import generator
mainlist=[]
for i in Namelist:
    for j in Birthdaylist:
        for k in charlist:
            mainlist+=generator.generator(i,j,k)
            for m in generator.generator(i,j,k):
                print(''.join(m))
                passfile.write(''.join(m)+'\n')
passfile.close()
print(len(mainlist))



