from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('Scrapper/', include('Craiglist.urls')),
    path('Todo/', include('Todo.urls')),
    path('admin/', admin.site.urls),
]
