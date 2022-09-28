"""seshat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

try:
    urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("seshat.apps.core.urls")),
    path('profiles/', include("seshat.apps.accounts.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('crisisdb/', include('seshat.apps.crisisdb.urls')),
    path('api/', include('seshat.apps.seshat_api.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
except:
    print("ERROR in including one of the url paths above...")
    urlpatterns=[]

urlpatterns += [
    path('__debug__/', include('debug_toolbar.urls')),
]
