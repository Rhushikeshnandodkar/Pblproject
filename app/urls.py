from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('bookdetail/<int:pk>', views.bookdetail, name="bookdetail"),

]