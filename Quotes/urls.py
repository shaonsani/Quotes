from django.conf.urls import url
from django.urls import path
from . import views

app_name='APP'

urlpatterns = [
   path('',views.Quotes_form, name='index'),
   path('<int:id>/',views.Quotes_form, name='update'),
   path('list/',views.Quotes_list, name='list'),
   path('delete/<int:id>',views.Quotes_delete, name='delete'),


]
