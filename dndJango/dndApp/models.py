# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Team(models.Model):
	teamId = models.CharField(max_length=100)
	description = models.CharField(max_length=2000)
	title = models.CharField(max_length=100, default='title')

	def __str__(self):
		return self.teamId

class Level(models.Model):
	levelId = models.CharField(max_length=100)
	description = models.CharField(max_length=2000)
	title = models.CharField(max_length=100, default='title')

	def __str__(self):
		return self.levelId

class Product(models.Model):
	productId = models.CharField(max_length=100)
	description = models.CharField(max_length=2000)
	title = models.CharField(max_length=100, default='title')

	def __str__(self):
		return self.productId

class Channel(models.Model):
	channelId = models.CharField(max_length=100)
	description = models.CharField(max_length=2000)
	title = models.CharField(max_length=100, default='title')

	def __str__(self):
		return self.channelId

class Payperiod(models.Model):
	payperiodId = models.CharField(max_length=100)
	description = models.CharField(max_length=2000)
	title = models.CharField(max_length=100, default='title')

	def __str__(self):
		return self.payperiodId

class Component(models.Model):
	componentId = models.CharField(max_length=100)
	description = models.CharField(max_length=2000)
	title = models.CharField(max_length=100, default='title')

	def __str__(self):
		return self.componentId
