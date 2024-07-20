from django.urls import path

from . import views
urlpatterns = [
    path("customerlogin", views.customerlogin, name="customerlogin")
]