from django.urls import path
from .views import todos_list, todo_detail, create_todo, delete_todo

urlpatterns = [
    path('', todos_list, name='todos_list'),
    path('<int:id>/', todo_detail, name='todo_detail'),
    path('create/', create_todo, name='create_todo'),
    path('<int:id>/delete/', delete_todo, name='delete_todo'),
]
