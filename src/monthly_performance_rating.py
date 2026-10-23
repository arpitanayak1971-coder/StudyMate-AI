class MonthlyPerformanceRating:

    def calculate_rating(
        self,
        goal_minutes,
        actual_minutes,
        session_count
    ):
        if goal_minutes <= 0:
            goal_score = 0
        else:
            goal_score = min(
                (actual_minutes / goal_minutes) * 100,
                100
            )

        # Score based on total study time
        if actual_minutes >= 1500:
            time_score = 100
        else:
            time_score = (actual_minutes / 1500) * 100

        # Score based on number of study sessions
        if session_count >= 20:
            session_score = 100
        else:
            session_score = (session_count / 20) * 100

        overall_score = (
            goal_score * 0.50
            + time_score * 0.30
            + session_score * 0.20
        )

        if overall_score >= 90:
            rating = "Excellent"
        elif overall_score >= 75:
            rating = "Very Good"
        elif overall_score >= 60:
            rating = "Good"
        elif overall_score >= 40:
            rating = "Needs Improvement"
        else:
            rating = "Poor"

        return {
            "overall_score": round(overall_score, 2),
            "rating": rating,
            "goal_score": round(goal_score, 2),
            "time_score": round(time_score, 2),
            "session_score": round(session_score, 2)
        }