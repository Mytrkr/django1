from django.conf.urls import url
from .views import *

app_name = 'accounts'

urlpatterns = [

    url(r'login/', _Login, name = 'login'),
    
]
