import json
from pathlib import Path
from datetime import date


class MonthlyGoalTracker:

    def __init__(self, goal_file="data/monthly_goals.json"):
        self.goal_file = Path(goal_file)
        self.goal_file.parent.mkdir(parents=True, exist_ok=True)

        if not self.goal_file.exists():
            self.goal_file.write_text("{}", encoding="utf-8")

    def _month_key(self, reference_date=None):
        if reference_date is None:
            reference_date = date.today()
        else:
            reference_date = date.fromisoformat(str(reference_date)[:10])

        return reference_date.strftime("%Y-%m")

    def _load_goals(self):
        try:
            with self.goal_file.open("r", encoding="utf-8") as file:
                data = json.load(file)
            return data if isinstance(data, dict) else {}
        except (json.JSONDecodeError, OSError):
            return {}

    def set_monthly_goal(self, minutes, reference_date=None):
        if isinstance(minutes, bool) or not isinstance(minutes, (int, float)):
            raise ValueError("Goal must be a positive number.")

        if minutes <= 0:
            raise ValueError("Goal must be greater than zero.")

        goals = self._load_goals()
        month_key = self._month_key(reference_date)
        goals[month_key] = minutes

        with self.goal_file.open("w", encoding="utf-8") as file:
            json.dump(goals, file, indent=4)

        return minutes

    def get_monthly_goal(self, reference_date=None):
        goals = self._load_goals()
        month_key = self._month_key(reference_date)
        return goals.get(month_key, 0)
