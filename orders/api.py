from rest_framework import viewsets
from .models import Orders
from goods.models import Goods
from .serializers import OrdersSerializer
from django.db.models import F
from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from time import sleep
from rest_framework.decorators import list_route
import requests
import random

class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    
    pagination_class = PageNumberPagination
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            goods_id = serializer.validated_data['goods_id']
            goods_num = serializer.validated_data['goods_num']
            goods = Goods.objects.get(pk=goods_id)
            if goods.goods_num < goods_num:
                return Response({'msg':'库存不足'}, status=status.HTTP_400_BAD_REQUEST)
            sleep(3)
            row = Goods.objects.filter(pk=goods_id,goods_num__gt=0).update(goods_num=F('goods_num')-goods_num)
            if row==0:
                return Response({'msg':'库存不足'}, status=status.HTTP_400_BAD_REQUEST)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except Goods.DoesNotExist:
            return Response({'msg':'商品不存在'}, status=status.HTTP_400_BAD_REQUEST)
        
    
    @list_route(methods=['POST'])
    def add_order(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except ValueError as e:
            return Response({'msg':e}, status=status.HTTP_400_BAD_REQUEST)
        
    @list_route(methods=['GET'])
    def batch(self,request, *args, **kwargs):
        order_no = random.randint(1000,2000)
        data = {'order_no':order_no,'order_price':4.5,'goods_id':1,'goods_num':1}
        url = "http://127.0.0.1:8888/orders/"
        re = requests.post(url=url,data=data)
        return Response({re.status_code}, status=status.HTTP_200_OK)
 
    
    