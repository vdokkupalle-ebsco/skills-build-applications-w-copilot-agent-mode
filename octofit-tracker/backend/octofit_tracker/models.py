from djongo import models
from bson import ObjectId

class User(models.Model):
	_id = models.ObjectIdField(primary_key=True, editable=False, default=ObjectId)
	username = models.CharField(max_length=100, unique=True)
	email = models.EmailField(unique=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	team = models.CharField(max_length=100)
	def __str__(self):
		return self.username

class Team(models.Model):
	_id = models.ObjectIdField(primary_key=True, editable=False, default=ObjectId)
	name = models.CharField(max_length=100, unique=True)
	members = models.JSONField(default=list)
	def __str__(self):
		return self.name

class Activity(models.Model):
	_id = models.ObjectIdField(primary_key=True, editable=False, default=ObjectId)
	user = models.CharField(max_length=100)
	activity = models.CharField(max_length=100)
	duration = models.IntegerField()
	def __str__(self):
		return f"{self.user} - {self.activity}"

class Leaderboard(models.Model):
	_id = models.ObjectIdField(primary_key=True, editable=False, default=ObjectId)
	user = models.CharField(max_length=100)
	points = models.IntegerField()
	def __str__(self):
		return f"{self.user}: {self.points}"

class Workout(models.Model):
	_id = models.ObjectIdField(primary_key=True, editable=False, default=ObjectId)
	name = models.CharField(max_length=100)
	difficulty = models.CharField(max_length=50)
	def __str__(self):
		return self.name
