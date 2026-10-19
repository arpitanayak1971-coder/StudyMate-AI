class MonthlyStudyReport:

    def __init__(self, analytics):
        self.analytics = analytics

    def generate_report(self, reference_date=None):
        total = self.analytics.total_monthly_minutes(reference_date)
        sessions = self.analytics.total_monthly_sessions(reference_date)
        average = self.analytics.average_session_minutes(reference_date)
        top_subject = self.analytics.most_studied_subject(reference_date)
        subjects = self.analytics.study_time_by_subject(reference_date)

        print("\n====== MONTHLY STUDY REPORT ======")
        print(f"Total Study Time: {total:g} minutes")
        print(f"Total Sessions: {sessions}")
        print(f"Average Session Duration: {average:.2f} minutes")
        print(f"Most Studied Subject: {top_subject or 'None'}")

        print("\nStudy Time by Subject:")

        if not subjects:
            print("No study sessions recorded for this month.")
        else:
            for subject, minutes in subjects.items():
                print(f"- {subject}: {minutes:g} minutes")

        print("==================================")
