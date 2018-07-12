# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Team, Level, Product, Channel, Payperiod, Component
from .serializers import TeamSerializer, LevelSerializer, ProductSerializer, ChannelSerializer, PayperiodSerializer, ComponentSerializer

# Create your views here.

class TeamList(APIView):
	def get(self, request):
		team = Team.objects.all()
		serializer = TeamSerializer(team, many=True)
		return Response(serializer.data)

	def post(self, request):
		teamSerializer = TeamSerializer(data=request.data)
		if teamSerializer.is_valid():
			teamSerializer.save()
			return Response(teamSerializer.data, status=status.HTTP_201_CREATED)
		return Response(teamSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LevelList(APIView):
	def get(self, request):
		level = Level.objects.all()
		serializer = LevelSerializer(level, many=True)
		return Response(serializer.data)

	def post(self, request):
		levelSerializer = LevelSerializer(data=request.data)
		if levelSerializer.is_valid():
			levelSerializer.save()
			return Response(levelSerializer.data, status=status.HTTP_201_CREATED)
		return Response(levelSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductList(APIView):
	def get(self, request):
		product = Product.objects.all()
		serializer = ProductSerializer(product, many=True)
		return Response(serializer.data)

	def post(self, request):
		productSerializer = ProductSerializer(data=request.data)
		if productSerializer.is_valid():
			productSerializer.save()
			return Response(productSerializer.data, status=status.HTTP_201_CREATED)
		return Response(productSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChannelList(APIView):
	def get(self, request):
		channel = Channel.objects.all()
		serializer = ChannelSerializer(channel, many=True)
		return Response(serializer.data)

	def post(self, request):
		channelSerializer = ChannelSerializer(data=request.data)
		if channelSerializer.is_valid():
			channelSerializer.save()
			return Response(channelSerializer.data, status=status.HTTP_201_CREATED)
		return Response(channelSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PayperiodList(APIView):
	def get(self, request):
		payperiod = Payperiod.objects.all()
		serializer = PayperiodSerializer(payperiod, many=True)
		return Response(serializer.data)

	def post(self, request):
		payperiodSerializer = PayperiodSerializer(data=request.data)
		if payperiodSerializer.is_valid():
			payperiodSerializer.save()
			return Response(payperiodSerializer.data, status=status.HTTP_201_CREATED)
		return Response(payperiodSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ComponentList(APIView):
	def get(self, request):
		component = Component.objects.all()
		serializer = ComponentSerializer(component, many=True)
		return Response(serializer.data)

	def post(self, request):
		componentSerializer = ComponentSerializer(data=request.data)
		if componentSerializer.is_valid():
			componentSerializer.save()
			return Response(componentSerializer.data, status=status.HTTP_201_CREATED)
		return Response(componentSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
