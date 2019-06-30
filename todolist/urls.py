from django.urls import path, include
from . import views

app_name = 'todolist'

urlpatterns = [
    path('home/', views.home, name='主页'),
    path('about/', views.about, name='关于'),
    path('edit/<event_id>', views.edit, name='编辑'),
    path('del/<event_id>', views.delete, name='删除'),
    path('cross/<event_id>', views.cross, name='划掉'),

]
