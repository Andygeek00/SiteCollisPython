
from django.contrib import admin
from django.urls import path
from app.views import *


urlpatterns = [
    path('', home_page),
    path('parcels/',parcels_page),
    path('tracking/',tracking_page),
    path('register/',add_parcels),
    path('admin/', admin.site.urls)
]
