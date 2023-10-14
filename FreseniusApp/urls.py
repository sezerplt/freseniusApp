from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("excelUpload/",views.excelUpload,name="excelUpload")
]