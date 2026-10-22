class MonthlyGoalInsights:

    def analyze_progress(self, goal_minutes, actual_minutes):
        if goal_minutes <= 0:
            return {
                "completion_percentage": 0.0,
                "status": "Not Set",
                "remaining_minutes": 0.0
            }

        actual_minutes = max(actual_minutes, 0)
        percentage = (actual_minutes / goal_minutes) * 100
        remaining = max(goal_minutes - actual_minutes, 0)

        if percentage >= 100:
            status = "Goal Achieved"
        elif percentage >= 75:
            status = "Almost There"
        elif percentage >= 25:
            status = "Making Progress"
        else:
            status = "Just Started"

        return {
            "completion_percentage": round(percentage, 2),
            "status": status,
            "remaining_minutes": round(remaining, 2)
        }
