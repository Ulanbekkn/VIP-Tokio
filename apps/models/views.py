from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Model, Review
from .serializers import ModelSerializer, ModelDetailSerializer, ModelValidateSerializer, ReviewSerializer
from .permissions import *


class ModelAPIView(ListCreateAPIView):
    queryset = Model.objects.all()
    pagination_class = PageNumberPagination
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ModelSerializer
        elif self.request.method == 'POST':
            return ModelDetailSerializer

    def post(self, request, *args, **kwargs):
        serializer = ModelValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        model = Model.objects.create(**serializer.validated_data)

        return Response(data=ModelSerializer(model).data)


class ModelDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelDetailSerializer
    permission_classes = [IsAdminOrReadOnly]

    def put(self, request, *args, **kwargs):
        serializer = ModelValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        model = Model.objects.all()
        serializer.update(model, serializer.validated_data)

        return Response(data=ModelSerializer(model).data)


class ReviewAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
