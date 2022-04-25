from django.shortcuts import render
from django.http import HttpResponse


def accounts(request):
    return HttpResponse('<h1>Hello Accounts.</h1>')
