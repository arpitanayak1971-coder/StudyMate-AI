import pandas as pd


class WeeklyStudyAnalytics:

    def __init__(self, study_data):
        self.study_data = study_data.copy()

        if not self.study_data.empty:
            self.study_data["date"] = pd.to_datetime(
                self.study_data["date"], errors="coerce"
            )
            self.study_data["duration_minutes"] = pd.to_numeric(
                self.study_data["duration_minutes"], errors="coerce"
            )

            self.study_data = self.study_data.dropna(
                subset=["date", "duration_minutes"]
            )

            self.study_data = self.study_data[
                self.study_data["duration_minutes"] > 0
            ].copy()

    def daily_study_minutes(self, reference_date=None):
        """Return study minutes for each day of the Monday-Sunday week."""
        if reference_date is None:
            reference_date = pd.Timestamp.today().normalize()
        else:
            reference_date = pd.Timestamp(reference_date).normalize()

        week_start = reference_date - pd.Timedelta(
            days=reference_date.weekday()
        )
        week_end = week_start + pd.Timedelta(days=6)

        days = pd.date_range(week_start, week_end, freq="D")
        daily_totals = {day.strftime("%A"): 0.0 for day in days}

        if self.study_data.empty:
            return daily_totals

        dates = self.study_data["date"].dt.normalize()
        weekly_data = self.study_data[
            (dates >= week_start) & (dates <= week_end)
        ].copy()

        if weekly_data.empty:
            return daily_totals

        weekly_data["day"] = weekly_data["date"].dt.day_name()
        totals = weekly_data.groupby("day")["duration_minutes"].sum()

        for day, minutes in totals.items():
            daily_totals[day] = float(minutes)

        return daily_totals

    def total_weekly_minutes(self, reference_date=None):
        return sum(self.daily_study_minutes(reference_date).values())

    def average_daily_minutes(self, reference_date=None):
        return self.total_weekly_minutes(reference_date) / 7

    def most_productive_day(self, reference_date=None):
        daily_totals = self.daily_study_minutes(reference_date)

        if not daily_totals or max(daily_totals.values()) == 0:
            return None

        return max(daily_totals, key=daily_totals.get)

    def least_productive_day(self, reference_date=None):
        daily_totals = self.daily_study_minutes(reference_date)
        studied_days = {
            day: minutes for day, minutes in daily_totals.items()
            if minutes > 0
        }

        if not studied_days:
            return None

        return min(studied_days, key=studied_days.get)

    def study_consistency(self, reference_date=None):
        daily_totals = self.daily_study_minutes(reference_date)
        active_days = sum(1 for minutes in daily_totals.values() if minutes > 0)

        return {
            "active_days": active_days,
            "total_days": 7,
            "consistency_percentage": round((active_days / 7) * 100, 2)
        }

    def weekly_performance_score(self, weekly_goal_minutes=600,
                                 reference_date=None):
        if weekly_goal_minutes <= 0:
            raise ValueError("Weekly goal must be greater than zero.")

        total = self.total_weekly_minutes(reference_date)
        score = min((total / weekly_goal_minutes) * 100, 100)

        return {
            "score": round(score, 2),
            "goal_minutes": weekly_goal_minutes,
            "studied_minutes": round(total, 2),
            "goal_achieved": total >= weekly_goal_minutes
        }

    def weekly_recommendations(self, weekly_goal_minutes=600,
                               reference_date=None):
        total = self.total_weekly_minutes(reference_date)
        consistency = self.study_consistency(reference_date)
        daily_totals = self.daily_study_minutes(reference_date)

        recommendations = []

        if total == 0:
            recommendations.append(
                "No study sessions recorded this week. Start with a short session."
            )
        elif total < weekly_goal_minutes:
            remaining = weekly_goal_minutes - total
            recommendations.append(
                f"Study {remaining:.0f} more minutes to reach your weekly goal."
            )
        else:
            recommendations.append(
                "Great work! You achieved your weekly study goal."
            )

        if consistency["active_days"] < 5:
            recommendations.append(
                "Try studying on at least five days each week."
            )

        if daily_totals and max(daily_totals.values()) > 0:
            best_day = max(daily_totals, key=daily_totals.get)
            worst_day = self.least_productive_day(reference_date)

            if worst_day:
                recommendations.append(
                    f"Improve your study routine on {worst_day}."
                )

        return recommendations

