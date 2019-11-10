"""pic2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import os
from django.conf.urls.static import static
from django.conf import settings

from django.views.static import serve


from picT.views import uploadImg,showImg,showFace,downLoad,index,uploadImg2,showImg2
from django.conf.urls import url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, 'picF1').replace('\\', '/') # media即为图片上传的根路径
MEDIA_URL = '/picF1/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',uploadImg2),
    path('showImg/', showImg),
    path('showFace/', showFace),
    path('downLoad/',downLoad),
    path('uploadImg2',showImg2)
    #path('change/',change),
]
