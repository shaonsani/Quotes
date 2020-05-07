from django.conf.urls import url
from django.urls import path
from . import views

app_name='APP'

urlpatterns = [
   path('add/',views.Quotes_form, name='index'),
   path('add/<int:id>/',views.Quotes_form, name='update'),
   path('',views.Quotes_list, name='list'),
   path('<int:id>/',views.Quotes_delete, name='delete'),


]
