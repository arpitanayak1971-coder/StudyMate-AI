import pandas as pd


class MonthlyStudyAnalytics:

    def __init__(self, study_data):
        self.study_data = study_data.copy()

        if not self.study_data.empty:
            self.study_data["date"] = pd.to_datetime(
                self.study_data["date"],
                format="%Y-%m-%d %H:%M:%S",
                errors="coerce"
            )
            self.study_data["duration_minutes"] = pd.to_numeric(
                self.study_data["duration_minutes"], errors="coerce"
            )

            self.study_data = self.study_data.dropna(
                subset=["date", "duration_minutes", "subject"]
            )

            self.study_data = self.study_data[
                self.study_data["duration_minutes"] > 0
            ].copy()

    def _get_month_data(self, reference_date=None):
        if reference_date is None:
            reference_date = pd.Timestamp.today()
        else:
            reference_date = pd.Timestamp(reference_date)

        if self.study_data.empty:
            return self.study_data.copy()

        return self.study_data[
            (self.study_data["date"].dt.year == reference_date.year)
            & (self.study_data["date"].dt.month == reference_date.month)
        ].copy()

    def total_monthly_minutes(self, reference_date=None):
        month_data = self._get_month_data(reference_date)
        return float(month_data["duration_minutes"].sum())

    def total_monthly_sessions(self, reference_date=None):
        return len(self._get_month_data(reference_date))

    def average_session_minutes(self, reference_date=None):
        month_data = self._get_month_data(reference_date)

        if month_data.empty:
            return 0.0

        return float(month_data["duration_minutes"].mean())

    def study_time_by_subject(self, reference_date=None):
        month_data = self._get_month_data(reference_date)

        if month_data.empty:
            return {}

        return (
            month_data.groupby("subject")["duration_minutes"]
            .sum()
            .sort_values(ascending=False)
            .to_dict()
        )

    def most_studied_subject(self, reference_date=None):
        subject_totals = self.study_time_by_subject(reference_date)

        if not subject_totals:
            return None

        return max(subject_totals, key=subject_totals.get)
