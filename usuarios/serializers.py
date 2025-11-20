from rest_framework import serializers
from .models import Usuario
from django.contrib.auth.password_validation import validate_password

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Usuario
        fields = ('id', 'username', 'email', 'tipo', 'password', 'password2', 'telefono', 'direccion')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Las contraseñas no coinciden."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = Usuario.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            tipo=validated_data['tipo'],
            telefono=validated_data.get('telefono', ''),
            direccion=validated_data.get('direccion', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
