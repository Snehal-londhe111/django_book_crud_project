from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.InsertView, name='insertview'),
    path("insert/", views.InsertData, name='insert'),
    path("showdata/", views.ShowData, name='showdata')
]
