from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
import re
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class YourTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    username = serializers.CharField(min_length=4)
    password = serializers.CharField()
    password2 = serializers.CharField()
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    email2 = serializers.EmailField()

    def validate(self, attrs):

        if attrs.get('password') != attrs.get('password2'):
            raise serializers.ValidationError('Пароли не совпадают!')

        if attrs.get('email') != attrs.get('email2'):
            raise serializers.ValidationError('Почты не совпадают!')

        return attrs

    @staticmethod
    def validate_username(username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        return ValidationError('user already exist!')

    @staticmethod
    def validate_password(password):
        if re.match("^(?=.*?[a-z])(?=.*?[0-9]).{8,}$", password):
            return password
        raise ValidationError('The password must consist of at least letters and numbers!')

    def create(self, validated_data):
        first_name = validated_data.get('first_name')
        username = validated_data.get('username')
        password = validated_data.get('password')
        email = validated_data.get('email')
        user = User.objects.create_user(first_name=first_name, username=username,
                                        password=password, email=email)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=4)
    password = serializers.CharField()


class ResetSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ResetConfirmPasswordSerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField()


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField()
    password_2 = serializers.CharField()

    def validate(self, attrs):

        if attrs.get('password') != attrs.get('password_2'):
            raise serializers.ValidationError('Пароли не совпадают!')

        return attrs

    @staticmethod
    def validate_password(password):
        if re.match("^(?=.*?[a-z])(?=.*?[0-9]).{8,}$", password):
            return password
        raise ValidationError('The password must consist of at least letters and numbers!')


class UserProfileSerializer(serializers.ModelSerializer):
    last_visit = serializers.DateTimeField()

    class Meta:
        model = User
        fields = 'id first_name username date_joined last_visit'.split()

