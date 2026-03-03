from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ('id', 'email', 'full_name', 'password')

    def create(self, validated_data):
        return User.objects.create_user(
            email=validated_data['email'],
            full_name=validated_data.get('full_name', ''),
            password=validated_data['password'],
        )


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('email', 'full_name', 'password', 'avatar')
        extra_kwargs = {
            'avatar': {'required': False, 'allow_null': True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'full_name', 'password')

    def create(self, validated_data):
        return User.objects.create_user(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            password=validated_data['password'],
        )

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'full_name', 'role']
        extra_kwargs = {
            'role': {'required': False, 'allow_null': True}
        }
    def update(self, instance, validated_data):
        instance.role = validated_data.get('role', instance.role)
        instance.save()
        return instance

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        from django.contrib.auth import authenticate
        request = self.context.get('request')
        user = authenticate(request, email=data['email'], password=data['password'])
        if user and user.is_active:
            data['user'] = user
            return data
        raise serializers.ValidationError("Invalid credentials")



class AuthResponseSerializer(serializers.Serializer):
    token = serializers.CharField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(read_only=True)
    full_name = serializers.CharField(read_only=True)