from . models import MyStu


# 将输入的邮箱和密码存在数据库里

def saveInfo(name,id,address,sex,date):
   MyStu(name=name, number=id, address=address, sex=sex, date=date).save()
