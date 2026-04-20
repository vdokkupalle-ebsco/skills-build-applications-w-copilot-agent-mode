from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models as djongo_models
from django.conf import settings
from pymongo import MongoClient

# Sample data for superheroes and teams
USERS = [
    {"username": "ironman", "email": "ironman@marvel.com", "first_name": "Tony", "last_name": "Stark", "team": "marvel"},
    {"username": "captainamerica", "email": "cap@marvel.com", "first_name": "Steve", "last_name": "Rogers", "team": "marvel"},
    {"username": "batman", "email": "batman@dc.com", "first_name": "Bruce", "last_name": "Wayne", "team": "dc"},
    {"username": "wonderwoman", "email": "wonderwoman@dc.com", "first_name": "Diana", "last_name": "Prince", "team": "dc"},
]

TEAMS = [
    {"name": "marvel", "members": ["ironman", "captainamerica"]},
    {"name": "dc", "members": ["batman", "wonderwoman"]},
]

ACTIVITIES = [
    {"user": "ironman", "activity": "Running", "duration": 30},
    {"user": "batman", "activity": "Cycling", "duration": 45},
    {"user": "wonderwoman", "activity": "Swimming", "duration": 60},
    {"user": "captainamerica", "activity": "Rowing", "duration": 25},
]

LEADERBOARD = [
    {"user": "ironman", "points": 100},
    {"user": "batman", "points": 90},
    {"user": "wonderwoman", "points": 80},
    {"user": "captainamerica", "points": 70},
]

WORKOUTS = [
    {"name": "Full Body", "difficulty": "Medium"},
    {"name": "Cardio Blast", "difficulty": "Hard"},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Insert users and create unique index on email
        db.users.insert_many(USERS)
        db.users.create_index([('email', 1)], unique=True)

        db.teams.insert_many(TEAMS)
        db.activities.insert_many(ACTIVITIES)
        db.leaderboard.insert_many(LEADERBOARD)
        db.workouts.insert_many(WORKOUTS)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
