"""tutorial_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


"""
    Please note that this is defined as the index. Any path in here will be defined by the first argument ('')  
    being the home and the include statement to the web apps defined url pattern. 
    This is essentially the master path. Do not confuse it with the paths dedicated within each web app's urls file 
"""
urlpatterns = [
    path('', include('travello.urls')),    
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls'))
] 

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)