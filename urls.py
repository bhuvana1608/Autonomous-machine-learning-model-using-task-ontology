"""Taskontology URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from Taskontology.views import adminlogin, adminloginaction, logout, userdetails, activateuser, userfiles, adminhome
from user.views import index, base, registration, user, userlogincheck, userhome, uploadfile, viewuserfiles, \
    findvocabulary, detection, imagedetect

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^index/', index, name="index"),
    url(r'^base/', base, name="base"),
    url(r'^registration/', registration, name="registration"),
    url(r'^user/', user, name="user"),
    url(r'^adminhome/', adminhome, name="adminhome"),
    url(r'^adminlogin/', adminlogin, name="adminlogin"),
    url(r'^adminloginaction/', adminloginaction, name="adminloginaction"),
    url(r'^logout/', logout, name="logout"),
    url(r'^userdetails/', userdetails, name="userdetails"),
    url(r'^userfiles/', userfiles, name="userfiles"),
    url(r'^activateuser/', activateuser, name="activateuser"),
    url(r'^userlogincheck/', userlogincheck, name="userlogincheck"),
    url(r'^userhome/', userhome, name="userhome"),
    url(r'^uploadfile/', uploadfile, name="uploadfile"),
    url(r'^viewuserfiles/', viewuserfiles, name="viewuserfiles"),
    url(r'^findvocabulary/', findvocabulary, name="findvocabulary"),
    url(r'^detection/', detection, name="detection"),
    url(r'^imagedetect', imagedetect, name="imagedetect")

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
