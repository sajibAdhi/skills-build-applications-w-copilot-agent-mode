from django.test import TestCase
from fitness.models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(email="test@example.com", name="Test User", age=25)
        self.assertEqual(user.email, "test@example.com")

class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name="Team A", members=["user1", "user2"])
        self.assertEqual(team.name, "Team A")

class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        activity = Activity.objects.create(user="user1", activity_type="running", duration=30)
        self.assertEqual(activity.activity_type, "running")

class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(user="user1", score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(name="Push-ups", description="Do 20 push-ups")
        self.assertEqual(workout.name, "Push-ups")
