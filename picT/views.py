from django.shortcuts import render
from picT.models import Img,Img2


# Create your views here.
#上传图片,Img是个model

def index(request):
    return render(request,'face.html')

def uploadImg(request): # 图片上传函数
    flag = '---'
    if request.method == 'POST':
        img = Img(img_url=request.FILES.get('img'))
        img.save()
        flag = '上传成功'
    return render(request, 'a.html',{"flag":flag})

def uploadImg2(request): # 图片上传函数
    flag2 = '---'
    if request.method == 'POST':
        Img2.objects.all().delete()
        img2 = Img2(img_url=request.FILES.get('img2'))
        img2.save()
    return render(request, 'face.html',{"flag":flag2})


#显示图片库图片
def showImg(request):
    imgs = Img.objects.all() # 从数据库中取出所有的图片路径
    context = {
        'imgs' : imgs
    }
    for i in imgs:
        print(i.img_url)
    return render(request, 'a.html',{'imgs':imgs})

def showImg2(request):
    imgs2 = Img2.objects.all() # 从数据库中取出所有的图片路径
    context = {
        'imgs2' : imgs2
    }
    for i in imgs2:
        print(i.img_url)
    return render(request, 'face.html',{'imgs2':imgs2})


#更换显示图片
#def change(request):


#根据网页地址下载图片，并随机命名
import string
import random
import urllib
#import requests
def downLoad(request):
    addr = request.POST.get("addr", None)
    print(addr)
    s = string.ascii_letters
    r = random.choice(s)
    i = random.randint(1,1000)
    i = str(i)
    x = r+i+'.jpg'
    #tt = requests.get(addr)
    x2='/Users/apple/PycharmProjects/pic2/picF3/' + x
    urllib.request.urlretrieve(addr, x2)
    return render(request,'a.html')

#人脸识别并显示图片
import os
import face_recognition
def showFace(request):
    imgs = Img.objects.all() # 从数据库中取出所有的图片路径
    # for i in imgs:
    #     x = str(i.img_url)
    #     print(type(x))
    # 加载目标图像
    image_to_be_matched = face_recognition.load_image_file('/Users/apple/PycharmProjects/pic2/picF2/a1.jpg')
    # 将加载图像编码为特征向量
    image_to_be_matched_encoded = face_recognition.face_encodings(image_to_be_matched)[0]
    #print(face_recognition.face_encodings(image_to_be_matched)[0])
    y = []
    for x in imgs:
        # 加载图像
        x1 = str(x.img_url)
        current_image = face_recognition.load_image_file('/Users/apple/PycharmProjects/pic2/'+x1)
        # 将加载图像编码为特征向量
        if face_recognition.face_encodings(current_image) == []:
            print(x1 + ":can not match")
            continue
        current_image_encoded = face_recognition.face_encodings(current_image)[0]
        # 将你的图像和图像对比，看是否为同一人
        result = face_recognition.compare_faces([image_to_be_matched_encoded], current_image_encoded)
        # 检查是否一致
        if result[0] == True:
            print("Matched: " + x1)
            y.append(x1)
            print(y)
        else:
            print("Not matched: " + x1)
    return render(request, 'a.html',{'face':y})


