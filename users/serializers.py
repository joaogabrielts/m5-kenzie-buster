from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'birthdate', 'first_name', 'last_name', 'is_employee', 'is_superuser', 'password']
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("email already registered.")
        return value
    
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("username already taken.")
        return value

    def update(self, instance, validated_data):
        # Permitir atualização apenas do próprio usuário ou se for um employee
        request_user = self.context['request'].user
        if not request_user.is_employee and request_user != instance:
            raise serializers.ValidationError("You do not have permission to update this user.")
        
        # Atualizar os campos normalmente
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
