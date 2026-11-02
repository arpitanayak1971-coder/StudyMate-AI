
class ImprovementInsights:
    def __init__(self, history):
        self.history = history

    def generate_insights(self):
        if not self.history:
            return ["No study history available. Record a snapshot first."]

        latest = self.history[-1]
        insights = []

        completion = latest["completion_percentage"]
        pending = latest["pending"]

        if completion >= 80:
            insights.append("Excellent progress! Keep maintaining your consistency.")
        elif completion >= 50:
            insights.append("Good progress. Try completing more pending tasks.")
        else:
            insights.append("Your completion rate is low. Set smaller daily targets.")

        if pending > 0:
            insights.append(
                f"You have {pending} pending tasks. Focus on completing them."
            )
        else:
            insights.append("Great! You have completed all recorded tasks.")

        if len(self.history) >= 2:
            previous = self.history[-2]
            change = completion - previous["completion_percentage"]

            if change > 0:
                insights.append(
                    f"Your completion rate improved by {change:.2f}%."
                )
            elif change < 0:
                insights.append(
                    f"Your completion rate decreased by {abs(change):.2f}%."
                )
            else:
                insights.append("Your completion rate remained unchanged.")

        return insights

    def display_insights(self):
        insights = self.generate_insights()

        print("\n====== SMART STUDY IMPROVEMENT INSIGHTS ======")

        for number, insight in enumerate(insights, start=1):
            print(f"{number}. {insight}")

        print("==============================================")

        return insights
        
