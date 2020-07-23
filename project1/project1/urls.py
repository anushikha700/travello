
"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from testapp.views import hello_jango
from timeapp.views import time_info
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('travello.urls')),
    path('testapp/', include('testapp.urls')),  #this include all urls of testapp eg: testapp/hello_world
    path('hello_jango/', hello_jango),
    path('time/', time_info),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    
]

urlpatterns= urlpatterns+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
