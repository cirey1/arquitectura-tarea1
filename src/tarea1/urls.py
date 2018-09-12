from django.urls import path

from tarea1.views import home_view, comment_view, comment_create_view

urlpatterns = [
    path('', home_view,name='home'),
    path('comments/', comment_view, name='comments'),
    path('create/', comment_create_view, name='create')
]
