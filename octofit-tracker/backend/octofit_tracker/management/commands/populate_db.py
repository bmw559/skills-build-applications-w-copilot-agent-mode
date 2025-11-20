from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Sample data
        users = [
            {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
            {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
            {"name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
            {"name": "Black Widow", "email": "widow@marvel.com", "team": "Marvel"},
        ]
        teams = [
            {"name": "Marvel", "members": ["ironman@marvel.com", "cap@marvel.com", "widow@marvel.com"]},
            {"name": "DC", "members": ["superman@dc.com", "batman@dc.com", "wonderwoman@dc.com"]},
        ]
        activities = [
            {"user_email": "superman@dc.com", "activity": "Flight", "duration": 60},
            {"user_email": "ironman@marvel.com", "activity": "Suit Training", "duration": 45},
        ]
        leaderboard = [
            {"team": "Marvel", "points": 150},
            {"team": "DC", "points": 120},
        ]
        workouts = [
            {"name": "Strength", "description": "General strength workout"},
            {"name": "Agility", "description": "Agility and speed drills"},
        ]

        # Insert sample data
        for u in users:
            User.objects.create(**u)
        for t in teams:
            Team.objects.create(**t)
        for a in activities:
            Activity.objects.create(**a)
        for l in leaderboard:
            Leaderboard.objects.create(**l)
        for w in workouts:
            Workout.objects.create(**w)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
