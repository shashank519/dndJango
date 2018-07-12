from rest_framework import serializers
from .models import Team, Level, Product, Channel, Payperiod, Component

class TeamSerializer(serializers.ModelSerializer):

	class Meta:
		model = Team
		fields = '__all__'

class LevelSerializer(serializers.ModelSerializer):

	class Meta:
		model = Level
		fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):

	class Meta:
		model = Product
		fields = '__all__'

class ChannelSerializer(serializers.ModelSerializer):

	class Meta:
		model = Channel
		fields = '__all__'

class PayperiodSerializer(serializers.ModelSerializer):

	class Meta:
		model = Payperiod
		fields = '__all__'

class ComponentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Component
		fields = '__all__'
