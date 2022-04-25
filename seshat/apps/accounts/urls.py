from django.urls import path, include

from . import views

urlpatterns = [
    #path('', views.accounts, name='accounts'),
    path('accounts/', include('django.contrib.auth.urls')),
]
