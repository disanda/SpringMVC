from django.db import models
import  string
import  random
import uuid
# Create your models here.
class Img(models.Model):
    def image_upload_to(instance, filename):
        s = string.ascii_letters
        r = random.choice(s)
        i = random.randint(1, 10000)
        i = str(i)
        x = r + i + '.jpg'
        return 'picF1/{filename}'.format(filename=x)
    img_url = models.ImageField(upload_to=image_upload_to) # upload_to指定图片上传的途径，如果不存在则自动创建

class Img2(models.Model):
    def image_upload_to(instance, filename):
        s = string.ascii_letters
        r = random.choice(s)
        i = random.randint(1, 10000)
        i = str(i)
        x = r + i + '.jpg'
        return 'picF2/{filename}'.format(filename='a1.jpg')
    img_url = models.ImageField(upload_to=image_upload_to) # upload_to指定图片上传的途径，如果不存在则自动创建