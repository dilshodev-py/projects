from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView, DestroyAPIView, RetrieveDestroyAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from app.models import User, Category, Product
from app.serializers import UserSerializer, CategoryListModelSerializer, ProductSerializer, ProductListModelSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    http_method_names = ['get']
    filter_backends = (OrderingFilter, DjangoFilterBackend, SearchFilter)
    ordering_fields = ('id', 'username')
    search_fields = ('username', 'email')
    filterset_fields = ('username', 'id')

    @action(detail=False, methods=['GET'])
    def get_me(self, requests, pk=None):
        if requests.user.is_authenticated:
            return Response({'message': f"{requests.user.username}"})
        return Response({'message': "Login qilinmagan !"})


class CategoryListViewSet(ListAPIView):
    serializer_class = CategoryListModelSerializer
    queryset = Category.objects.all()


class CategoryDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListModelSerializer
    http_method_names = ['get']


class ProductListViewSet(ListAPIView):
    serializer_class = ProductListModelSerializer
    queryset = Product.objects.filter(is_premium=True)
    filterset_fields = ('category',)
    http_method_names = ['get']


class ProductDeleteViewSet(RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError:
            return Response('Invalid data',
                            status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        return Response("Success !",
                        status=status.HTTP_201_CREATED)
