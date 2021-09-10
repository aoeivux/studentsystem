from os import name
from django.shortcuts import render
from . import service
from . models import MyStu
# Create your views here.

# 包含了登录功能
def index(request):
    return render(request, '../templates/index.html', {})



def response(request):
    # 将前端POST提交的内容获取上传到数据库

    # 姓名
    name = request.POST.get('name')
    
    # 学号
    id = request.POST.get('id') # number

    # 家庭地址    
    address = request.POST.get('address')

    #出生日期
    date = request.POST.get('date')
    
    # 性别
    sex = request.POST.get('sex')



    print(id)
    print(date)
    service.saveInfo(name, id, address, sex, date)
    listStudentName = []
    db = MyStu.objects.all()
   
    # name = models.CharField(max_length=255)
    # age = models.DateField()
    # sex = models.CharField(max_length=255)
    # address = models.CharField(max_length=255)
    # number = models.IntegerField()


    for i in db:
        listStudentName.append(i)
        print(i.date)
    return render(request, '../templates/response.html', {'resp':listStudentName})



def search(request):
    return render(request, '../templates/search.html', {})
