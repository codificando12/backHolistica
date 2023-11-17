from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Terapeutas, Terapia
from rest_framework import permissions
from terapeutas.permissions import IsOwnerOrReadOnly

class UserSerializer(serializers.ModelSerializer):
    terapeuta = serializers.PrimaryKeyRelatedField(many=True, queryset=Terapeutas.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'terapeuta']


class TerapeutasSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    class Meta:
        model = Terapeutas
        fields = ['id', 'register', 'name', 'last_name', 'owner', 'description', 'terapias']


class TerapiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terapia
        fields = "__all__"