from django.urls import path
from .views import list_students

urlpatterns = [
    path("", list_students),
]
