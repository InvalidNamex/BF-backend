from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('payment', views.payment_request),
]
