import json
import os
from datetime import date, datetime, timedelta


class StudyGoalTracker:
    def __init__(
        self,
        goal_file="data/study_goal.json",
        session_file="data/sessions.json"
    ):
        self.goal_file = goal_file
        self.session_file = session_file
        self.daily_goal_minutes = 120
        self.weekly_goal_minutes = 600
        self.load_goal()

    def load_goal(self):
        os.makedirs(os.path.dirname(self.goal_file), exist_ok=True)

        if os.path.exists(self.goal_file):
            with open(self.goal_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.daily_goal_minutes = data.get("daily_goal_minutes", 120)
                self.weekly_goal_minutes = data.get("weekly_goal_minutes", 600)

    def save_goals(self):
        with open(self.goal_file, "w", encoding="utf-8") as file:
            json.dump({
                "daily_goal_minutes": self.daily_goal_minutes,
                "weekly_goal_minutes": self.weekly_goal_minutes
            }, file, indent=4)

    def set_daily_goal(self, minutes):
        if isinstance(minutes, bool) or not isinstance(minutes, (int, float)):
            raise ValueError("Goal must be a positive number.")
        if minutes <= 0:
            raise ValueError("Goal must be greater than zero.")

        self.daily_goal_minutes = minutes
        self.save_goals()
        return self.daily_goal_minutes

    def get_today_study_minutes(self):
        if not os.path.exists(self.session_file):
            return 0

        with open(self.session_file, "r", encoding="utf-8") as file:
            sessions = json.load(file)

        today = date.today()
        total_minutes = 0

        for session in sessions:
            try:
                session_date = datetime.strptime(
                    session["date"], "%Y-%m-%d %H:%M:%S"
                ).date()
                if session_date == today:
                    total_minutes += float(session["duration_minutes"])
            except (KeyError, TypeError, ValueError):
                continue

        return total_minutes

    def get_goal_progress(self):
        studied_minutes = self.get_today_study_minutes()
        percentage = min(
            (studied_minutes / self.daily_goal_minutes) * 100, 100
        )

        return {
            "goal_minutes": self.daily_goal_minutes,
            "studied_minutes": studied_minutes,
            "remaining_minutes": max(
                self.daily_goal_minutes - studied_minutes, 0
            ),
            "completion_percentage": round(percentage, 2),
            "goal_achieved": studied_minutes >= self.daily_goal_minutes
        }

    def set_weekly_goal(self, minutes):
        if isinstance(minutes, bool) or not isinstance(minutes, (int, float)):
            raise ValueError("Weekly goal must be a positive number.")
        if minutes <= 0:
            raise ValueError("Weekly goal must be greater than zero.")

        self.weekly_goal_minutes = minutes
        self.save_goals()
        return self.weekly_goal_minutes

    def get_weekly_study_minutes(self):
        if not os.path.exists(self.session_file):
            return 0

        with open(self.session_file, "r", encoding="utf-8") as file:
            sessions = json.load(file)

        today = date.today()
        week_start = today - timedelta(days=today.weekday())
        total_minutes = 0

        for session in sessions:
            try:
                session_date = datetime.strptime(
                    session["date"], "%Y-%m-%d %H:%M:%S"
                ).date()

                if week_start <= session_date <= today:
                    total_minutes += float(session["duration_minutes"])
            except (KeyError, TypeError, ValueError):
                continue

        return total_minutes

    def get_weekly_goal_progress(self):
        goal = self.weekly_goal_minutes
        studied = self.get_weekly_study_minutes()

        return {
            "goal_minutes": goal,
            "studied_minutes": studied,
            "remaining_minutes": max(goal - studied, 0),
            "completion_percentage": round(min(studied / goal * 100, 100), 2),
            "goal_achieved": studied >= goal
        }
