from rest_framework import serializers
from .models import Support, MiniBlog


class SupportSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=20)
    mail = serializers.EmailField(max_length=50)
    subject = serializers.CharField(max_length=20)

    class Meta:
        model = Support
        fields = '__all__'


class MiniBlogSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=30)
    image = serializers.ImageField()
    description = serializers.CharField()

    class Meta:
        model = MiniBlog
        fields = '__all__'


class MiniBlogDetailSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = MiniBlog
        fields = ['id', 'title', 'image', 'description', 'user']


class AboutUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = MiniBlog
        fields = '__all__'

