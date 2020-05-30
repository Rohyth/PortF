from django.urls import path
from .views import todo, create_new, delete_item


urlpatterns = [
    path('', todo),
    path('delete_todo/<int:id>/', delete_item),
    path('create_new/', create_new),
]
