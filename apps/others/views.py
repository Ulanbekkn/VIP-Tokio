from .serializers import *
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.models.permissions import IsAdminOrReadOnly
from .permissions import IsOwnerOrReadOnly
from .models import AboutUs


class SupportAPIView(CreateAPIView):
    queryset = Support.objects.all()
    serializer_class = SupportSerializer


class MiniBlogAPIView(ListCreateAPIView):
    queryset = MiniBlog.objects.all()
    serializer_class = MiniBlogSerializer


class MiniBlogDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = MiniBlog.objects.all()
    serializer_class = MiniBlogSerializer
    permission_classes = [IsOwnerOrReadOnly, ]


class AboutUsAPIView(ListCreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsAdminOrReadOnly, ]

