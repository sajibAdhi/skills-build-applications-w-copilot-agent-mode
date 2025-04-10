from django.core.management.base import BaseCommand
from octofit_tracker.settings import MONGO_DB

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Populate users collection
        users = [
            {"email": "user1@example.com", "name": "User One", "password": "password1"},
            {"email": "user2@example.com", "name": "User Two", "password": "password2"},
        ]
        MONGO_DB.users.insert_many(users)

        # Populate teams collection
        teams = [
            {"name": "Team Alpha", "members": ["user1@example.com", "user2@example.com"]},
        ]
        MONGO_DB.teams.insert_many(teams)

        # Populate activities collection
        activities = [
            {"user": "user1@example.com", "activity_type": "Running", "duration": 30, "date": "2025-04-10"},
            {"user": "user2@example.com", "activity_type": "Cycling", "duration": 45, "date": "2025-04-09"},
        ]
        MONGO_DB.activity.insert_many(activities)

        # Populate leaderboard collection
        leaderboard = [
            {"user": "user1@example.com", "score": 100},
            {"user": "user2@example.com", "score": 150},
        ]
        MONGO_DB.leaderboard.insert_many(leaderboard)

        # Populate workouts collection
        workouts = [
            {"name": "Push-ups", "description": "Do 20 push-ups"},
            {"name": "Sit-ups", "description": "Do 30 sit-ups"},
        ]
        MONGO_DB.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
