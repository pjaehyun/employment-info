from django.urls import path
from . import views

app_name = "boards"

urlpatterns = [
    path("search/", views.search, name="search"),
]
