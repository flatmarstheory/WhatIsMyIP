from django.shortcuts import render
from django.http import HttpRequest


def show_ip(request: HttpRequest):
    user_ip = request.META.get('REMOTE_ADDR')
    return render(request, 'show_ip.html', {'user_ip': user_ip})
