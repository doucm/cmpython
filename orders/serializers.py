# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Orders

class OrdersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Orders
        #fields = ('__all__')
        
    
    def create(self, validated_data):
        try:
            data = validated_data
            print(data)
            return Orders.objects.add(data=data)
        except ValueError as e:
            raise serializers.ValidationError(str(e))
        
    def update(self, instance, validated_data):
        return serializers.ModelSerializer.update(self, instance, validated_data)
