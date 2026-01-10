from rest_framework import serializers
from .models import Workers
from django.contrib.auth.models import User

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workers
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","email","password"]
        extra_kwargs = {
            "password":{"write_only": True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data("email"),
            password=validated_data["password"]
        )
        # user.set_password(validated_data['password'])
        # user.save()
        # return user