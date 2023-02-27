from django.contrib.auth import authenticate
from djoser.serializers import (
    UserCreateSerializer as BaseUserCreateSerializer,
    UserSerializer as BaseUserSerializer
)

from rest_framework import serializers

from myowngame.models import CustomUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password




# class LoginSerializer(serializers.Serializer):
#     """
#     This serializer defines two fields for authentication:
#       * username
#       * password.
#     It will try to authenticate the user with when validated.
#     """
#     username = serializers.CharField(
#         label="Username",
#         write_only=True
#     )
#     password = serializers.CharField(
#         label="Password",
#         # This will be used when the DRF browsable API is enabled
#         style={'input_type': 'password'},
#         trim_whitespace=False,
#         write_only=True
#     )

#     def validate(self, attrs):
#         # Take username and password from request
#         username = attrs.get('username')
#         password = attrs.get('password')

#         if username and password:
#             # Try to authenticate the user using Django auth framework.
#             user = authenticate(request=self.context.get('request'),
#                                 username=username, password=password)
#             if not user:
#                 # If we don't have a regular user, raise a ValidationError
#                 msg = 'Access denied: wrong username or password.'
#                 raise serializers.ValidationError(msg, code='authorization')
#         else:
#             msg = 'Both "username" and "password" are required.'
#             raise serializers.ValidationError(msg, code='authorization')
#         # We have a valid user, put it in the serializer's validated_data.
#         # It will be used in the view.
#         attrs['user'] = user
#         return attrs


class UserSerializer(BaseUserSerializer):
    """
    Изменение сериализатора djoser работы с моделью User
    для отображение дополнительных полей.
    """
    class Meta(BaseUserSerializer.Meta):
        fields = (
            'username',
            'avatar',
            'gender',
            'count',
            'count_game',
        )


class RegisterSerializer(BaseUserCreateSerializer):
    """
    Изменение сериализатора djoser работы с моделью User
    при создании нового пользователя для отображение дополнительных полей.
    """
    class Meta(BaseUserCreateSerializer.Meta):
        fields = (
            'username',
            'avatar',
            'gender',
            'password')
                  
    # password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    # password2 = serializers.CharField(write_only=True, required=True)

    # class Meta:
    #     model = CustomUser
    #     fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'gender')
    #     extra_kwargs = {
    #         'first_name': {'required': True},
    #         'last_name': {'required': True}
    #     }

    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError({"password": "Password fields didn't match."})

    #     return attrs

    # def create(self, validated_data):
    #     user = CustomUser.objects.create(
    #         username=validated_data['username'],
    #         email=validated_data['email'],
    #         first_name=validated_data['first_name'],
    #         last_name=validated_data['last_name'],
    #         gender=validated_data['gender']
    #     )

    #     user.set_password(validated_data['password'])
    #     user.save()

    #     return user
