from django.urls import path
from . import views


urlpatterns = [
    path('', views.ModelAPIView.as_view()),
    path('<int:pk>/', views.ModelDetailAPIView.as_view()),

    # path('reviews/', views.ReviewApiView.as_view()),
    # path('reviews/<int:id_>/', views.ReviewDetailApiView.as_view()),
]
