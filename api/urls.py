from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('payment', views.payment_request),
    path('ai-payment', views.ai_payment_request),
]
