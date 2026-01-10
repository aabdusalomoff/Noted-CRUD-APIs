
from rest_framework import serializers
from .models import Note
from django.contrib.auth import get_user_model


User = get_user_model()
    

class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        user = User(username=username)
        user.set_password(password)
        user.save()
        return user
    

class NoteSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source = "created_by.id", read_only=True)
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'user_id']
