from django.contrib import admin
from django.urls import path
from nasa_apod.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index)
]

