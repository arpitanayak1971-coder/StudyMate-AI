class MonthlyGoalReport:

    def __init__(self, goal_tracker, analytics):
        self.goal_tracker = goal_tracker
        self.analytics = analytics

    def generate_report(self, reference_date=None):
        goal = self.goal_tracker.get_monthly_goal(reference_date)
        actual = self.analytics.total_monthly_minutes(reference_date)

        remaining = max(goal - actual, 0)
        percentage = (actual / goal * 100) if goal > 0 else 0

        print("\n====== MONTHLY GOAL VS ACTUAL ======")
        print(f"Monthly Goal: {goal:g} minutes")
        print(f"Actual Study Time: {actual:g} minutes")
        print(f"Remaining Study Time: {remaining:g} minutes")
        print(f"Goal Completion: {percentage:.2f}%")

        if goal <= 0:
            print("Set a monthly goal to track your progress.")
        elif actual >= goal:
            print("Congratulations! Monthly study goal achieved.")
        else:
            print("Keep going! You still have time to reach your goal.")

        print("====================================")
