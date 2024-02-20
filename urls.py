from django.urls import path
from .import views
urlpatterns=[
    path('',views.showRecords),# first page
    path('stdform',views.loadForm, name='loadForm'),
    path('insert',views.insertRecord),
    #path('show',views.showRecords), it is blank make it first page
    path('del<int:sid>',views.deleteRecord,name='delete'),
    path('get/<int:sid>',views.getRecordbyID,name='edit'),
    path('update/<int:sid>',views.updateRecord),
    ]