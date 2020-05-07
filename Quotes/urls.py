from django.conf.urls import url
from django.urls import path
from . import views

app_name='APP'

urlpatterns = [
   path('',views.employee_form, name='index'),
   path('<int:id>/',views.employee_form, name='update'),
   path('list/',views.employee_list, name='list'),
   path('delete/<int:id>',views.employee_delete, name='delete'),


]
