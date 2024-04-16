from rest_framework import serializers
from .models import Order, OrderDetail


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'  # Explicitly list fields instead of using '__all__' for better control


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'  # Explicitly list fields instead of using '__all__' for better control
