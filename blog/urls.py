from django.urls import path
from .views import index, course_delete, course_edit
 
urlpatterns= [
 path('', index, name='home'),
 path('<int:id>/delete', course_delete, name='course_delete'),
 path('<int:id>/edit/course', course_edit, name='course_edit')
] 