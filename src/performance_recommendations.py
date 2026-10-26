class PerformanceRecommendations:
    def generate_recommendations(self, result):
        recommendations = []

        goal_score = result["goal_score"]
        time_score = result["time_score"]
        session_score = result["session_score"]
        overall_score = result["overall_score"]
        rating = result["rating"]

        if goal_score < 60:
            recommendations.append(
                "Set a realistic monthly study goal and follow a weekly plan."
            )
        elif goal_score < 100:
            recommendations.append(
                "Keep working consistently to reach your monthly study goal."
            )
        else:
            recommendations.append(
                "Great goal achievement! Maintain your study consistency."
            )

        if time_score < 60:
            recommendations.append(
                "Increase focused study time gradually and schedule regular sessions."
            )
        elif time_score < 100:
            recommendations.append(
                "Try to reach your monthly study-time target."
            )
        else:
            recommendations.append(
                "You met the study-time target. Maintain a balanced routine."
            )

        if session_score < 60:
            recommendations.append(
                "Try shorter, more frequent study sessions throughout the week."
            )
        elif session_score < 100:
            recommendations.append(
                "Add a few more study sessions to improve consistency."
            )
        else:
            recommendations.append(
                "Excellent session consistency. Keep reviewing what you learn."
            )

        if overall_score >= 90:
            summary = "Excellent performance. Keep up your effective study habits."
        elif overall_score >= 75:
            summary = "Very good performance. Focus on the areas with lower scores."
        elif overall_score >= 60:
            summary = "Good progress. A consistent routine can help you improve."
        elif overall_score >= 40:
            summary = "Your progress can improve with clearer goals and regular practice."
        else:
            summary = "Start with small, achievable study targets and build consistency."

        return {
            "overall_score": overall_score,
            "rating": rating,
            "summary": summary,
            "recommendations": recommendations
        }
