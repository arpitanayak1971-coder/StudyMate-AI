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
