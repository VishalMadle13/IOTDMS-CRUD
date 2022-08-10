from ast import Delete
from django.urls import path
from . import views
urlpatterns = [
    path('',views.DeviceRegistar),
    path('show/',views.ShowData),
    path('send/',views.send),
    path('delete',views.delete),
    path('edit',views.edit),
    path('RecordEdited',views.RecordEdited),
    path('more',views.more)

    
]
