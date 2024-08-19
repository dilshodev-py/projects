from rest_framework.serializers import ModelSerializer

from app.models import User, Category, Product


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = ('username', 'email', 'id', 'age')
        exclude = ('groups', 'user_permissions')


class CategoryListModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ()

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ()

class ProductListModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ('description' , 'category')
