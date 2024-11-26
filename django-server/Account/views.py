from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from .models import User
from .serializers import UserSerializer
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter, OpenApiResponse
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .swagger_descriptions import account_endpoints, admin_account_endpoints

@account_endpoints["create"]
class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

@account_endpoints["me"]
class UserMeAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

@account_endpoints["update"]
class UserUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    http_method_names = ['put']

    def get_object(self):
        return self.request.user

@account_endpoints["token"]
class TokenObtainPair(TokenObtainPairView):
    pass

class UsersAPIListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000

@extend_schema_view(
    list=admin_account_endpoints["list"],
    retrieve=admin_account_endpoints["retrieve"],
    create=admin_account_endpoints["create"],
    update=admin_account_endpoints["update"],
    destroy=admin_account_endpoints["destroy"]
)
class AdminViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    pagination_class = UsersAPIListPagination
    http_method_names = ['get', 'post', 'put', 'delete']
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance == request.user:
            return Response(
                {"detail": "Администратор не может удалить сам себя."},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().destroy(request, *args, **kwargs)
