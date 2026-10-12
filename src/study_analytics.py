class StudyAnalytics:

    def __init__(self, study_data):
        self.study_data = study_data.copy()

    def total_study_minutes(self):
        if self.study_data.empty:
            return 0

        return self.study_data["duration_minutes"].sum()

    def total_sessions(self):
        return len(self.study_data)

    def average_session_minutes(self):
        if self.study_data.empty:
            return 0

        return self.study_data["duration_minutes"].mean()

    def study_time_by_subject(self):
        if self.study_data.empty:
            return {}

        return (
            self.study_data.groupby("subject")["duration_minutes"]
            .sum()
            .sort_values(ascending=False)
            .to_dict()
        )

    def most_studied_subject(self):
        subject_totals = self.study_time_by_subject()

        if not subject_totals:
            return None

        return max(subject_totals, key=subject_totals.get)
