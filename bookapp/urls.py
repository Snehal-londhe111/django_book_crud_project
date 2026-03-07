from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.InsertView, name='insertview'),
    path("insert/", views.InsertData, name='insert'),
    path("showdata/", views.ShowData, name='showdata'),
    path("editview/<int:pk>", views.EditView, name='editview'),
    path("updatedata/<int:pk>", views.UpdateData, name='update'),
    path("deletedata/<int:pk>", views.DeleteData, name='delete')
]
