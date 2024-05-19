from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User


class AccountSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'password2',
            'name',
            'gender',
            'birth_date',
            'email',
            'phone_number',
            'last_login',
            'date_joined',
            'is_superuser',
            'is_staff',
            'is_active',
        )
        read_only_fields = ('is_superuser', 'is_staff', 'is_active', 'date_joined', 'last_login')

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')

        if password != password2:
            raise serializers.ValidationError("Passwords do not match.")

        if len(password) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")

        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.password = make_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        validated_data.pop('password2', None)
        password = validated_data.pop('password', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.password = make_password(password)

        instance.save()
        return instance
