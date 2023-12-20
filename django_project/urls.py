from django.urls import path
from ip_app.views import show_ip

urlpatterns = [path('', show_ip, name='show_ip')]
