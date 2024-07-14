from rest_framework import serializers
from store.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']
        lookup_field = 'slug'


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['name', 'slug']
        lookup_field = 'slug'


class MaterialSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    unit = UnitSerializer()
    total_cost = serializers.SerializerMethodField(method_name='total')
    grand_total = serializers.SerializerMethodField(method_name='main_total')

    class Meta:
        model = Material
        fields = ['grand_total', 'id', 'name', 'slug', 'description' 'category' 'unit', 'quantity','price', 'total_cost']
        lookup_field = 'slug'

    def total(self, material: Material):
        return material.quantity * material.price

    def main_total(self, material: Material):
        items = Material.items.all()
        total = sum([item.quantity * item.price for item in items])
        return total

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['unit'] = [representation['unit']['name']]
        return representation