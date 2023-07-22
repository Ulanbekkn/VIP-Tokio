from django.urls import path
from .views import *


urlpatterns = [
    path('support/', SupportAPIView.as_view(), name="support"),
    path('miniblog/', MiniBlogAPIView.as_view(), name="miniblog"),
    path('miniblog/<int:pk>/', MiniBlogDetailAPIView.as_view(), name="miniblogdetail"),
    path('aboutus/', AboutUsAPIView.as_view(), name="aboutus"),
]


