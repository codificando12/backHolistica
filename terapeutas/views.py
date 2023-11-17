from rest_framework import viewsets, generics
from .serializers import TerapeutasSerializer, TerapiaSerializer, UserSerializer
from .models import Terapia, Terapeutas

from django.contrib.auth.models import User
from rest_framework import permissions

# Create your views here.

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TerapeutaViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Terapeutas.objects.all()
    serializer_class = TerapeutasSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TerapiaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Terapia.objects.all()
    serializer_class = TerapiaSerializer