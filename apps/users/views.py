from random import randint
from django.contrib.auth import logout
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from . import serializers
from rest_framework.permissions import AllowAny
from .utils import send_email
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.shortcuts import get_object_or_404
from apps.users.models import User
from .models import ResetPasswordConfirm


class ObtainTokenPairView(TokenObtainPairView):
    serializer_class = serializers.YourTokenObtainPairSerializer


class RegisterAPIView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.is_staff = False
        user.save()

        send_email(subject=f'Параметры учётной записи для {user.first_name} '
                           f'на сайте VIP Tokio проститутки Токтогула',
                   body=f'Здравствуйте {user.first_name}\n'
                           f'Спасибо за регистрацию на VIP Tokio проститутки Токтогула.\n'
                           f'Теперь вы можете войти на https://vip-tokio.com/ используя следующие данные:\n'
                           f'Логин: {user.username}',
                   to_email=[user.email])

        if send_email:
            return Response(data='Сообщение\n'
                                 'Спасибо за регистрацию. Теперь вы можете войти на сайт, '
                                 'используя логин и пароль, указанные при регистрации.',
                            status=status.HTTP_201_CREATED)
        user.delete()
        return Response(data=f'Problem sending email to {user.email}, check if you typed it correctly',
                        status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):
    serializer_class = serializers.LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user:
            refresh = RefreshToken.for_user(user)
            access = AccessToken.for_user(user)
            return Response({
                'user': user.username,
                'token': str(refresh),
                'access_token': str(access)
            })

        return Response(data='Неправильный логин или пароль!', status=status.HTTP_401_UNAUTHORIZED)


class ResetAPIVIew(GenericAPIView):
    serializer_class = serializers.ResetSerializer
    permission_classes = [AllowAny]


class ResetLoginAPIView(ResetAPIVIew):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')
        user = get_object_or_404(User, email=email)

        send_email(subject='Восстановление логина на сайте VIP Tokio проститутки Токтогула',
                   body=f'Здравствуйте, На сайте VIP Tokio проститутки Токтогула была сделана '
                        f'заявка на восстановление логина вашей учётной записи.\n'
                        f'Ваш логин: {user.username}.\n'
                        f'Для входа на сайт под вашими учётными данными перейдите по ссылке ниже.\n'
                        f'https://vip-tokio.com/register?view=login\nСпасибо.',
                   to_email=[email])

        if send_email:
            return Response(data={'message': 'Сообщение с информацией отправлено на указанный адрес. '
                                             'Пожалуйста, проверьте почту.'},
                            status=status.HTTP_200_OK)

        return Response(data='Не удалось отправить письмо для восстановления логина.',
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ResetPasswordAPIView(ResetAPIVIew):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')

        user = get_object_or_404(User, email=email)

        code = ResetPasswordConfirm.objects.create(username=user.username, code=str(randint(100000, 1000000)))
        send_email(subject='Запрос сброса пароля на сайте VIP Tokio проститутки Токтогула',
                   body=f'Здравствуйте,\n На сайте VIP Tokio проститутки был сделан запрос на '
                        f'восстановление пароля к вашей учётной записи. Чтобы восстановить пароль'
                        f' вам потребуется ввести указанный ниже код подтверждения.\n'
                        f'Код подтверждения: {code.code}.\n'
                        f'Для ввода кода подтверждения перейдите на страницу по ссылке ниже.\n'
                        f'https://vibish.com/reset?layout=confirm&token\nСпасибо.',
                   to_email=[email])

        if send_email:
            return Response(data='На ваш адрес электронной почты было отправлено письмо, содержащее проверочный код.'
                                 ' Введите его, пожалуйста, в поле ниже. '
                                 'Это подтвердит, что именно вы являетесь владельцем данной учётной записи.',
                            status=status.HTTP_200_OK)

        return Response(data='Не удалось отправить письмо для восстановления пароля.',
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ResetConfirmPasswordAPIView(GenericAPIView):
    serializer_class = serializers.ResetConfirmPasswordSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        code = serializer.validated_data.get('code')

        try:
            ResetPasswordConfirm.objects.get(username=username, code=code)
        except ResetPasswordConfirm.DoesNotExist:
            return Response(data={'detail': 'Не удалось восстановить пароль, поскольку проверочный код'
                                            ' был указан неверно. Пользователь не найден!'},
                            status=status.HTTP_404_NOT_FOUND)

        return Response(data={'username': username}, status=status.HTTP_200_OK)


class ChangePasswordAPIView(GenericAPIView):
    serializer_class = serializers.ChangePasswordSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = self.kwargs['username']
        user = get_object_or_404(User, username=username)

        user.set_password(serializer.validated_data.get('password'))  # Используем set_password() для изменения пароля
        user.save()
        return Response(data={'detail': 'Пароль успешно изменен'})


class LogoutAPIView(GenericAPIView):
    @staticmethod
    def post(request, *args, **kwargs):
        logout(request)

        return Response(data={'detail': 'Вы успешно вышли'})


class UserProfileAPIView(GenericAPIView):
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.UserProfileSerializer
        elif self.request.method == 'PUT':
            return serializers.RegisterSerializer

    def get(self, request, pk):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exceptions=True)

        user = User.objects.all()

        user.username = serializer.validated_data.get('username')
        user.first_name = serializer.validated_data.get('first_name')
        user.password = serializer.validated_data.get('password')
        user.email = serializer.validated_data.get('email')

        user.save()

        return Response(data={'detail': 'success'}, status=status.HTTP_201_CREATED)

