
class SubjectBalanceAnalyzer:

    def __init__(self, subject_data):
        self.subject_data = {
            subject: float(minutes)
            for subject, minutes in subject_data.items()
            if float(minutes) > 0
        }

    def total_study_time(self):
        return sum(self.subject_data.values())

    def subject_distribution(self):
        total = self.total_study_time()

        if total == 0:
            return {}

        return {
            subject: round((minutes / total) * 100, 2)
            for subject, minutes in self.subject_data.items()
        }

    def least_studied_subject(self):
        if not self.subject_data:
            return None

        return min(self.subject_data, key=self.subject_data.get)

    def most_studied_subject(self):
        if not self.subject_data:
            return None

        return max(self.subject_data, key=self.subject_data.get)

    def balance_score(self):
        distribution = self.subject_distribution()

        if len(distribution) < 2:
            return None

        equal_share = 100 / len(distribution)

        deviation = sum(
            abs(percentage - equal_share)
            for percentage in distribution.values()
        ) / 2

        score = max(0, 100 - (deviation / (100 - equal_share)) * 100)

        return round(score, 2)

    def recommendations(self):
        distribution = self.subject_distribution()

        if not distribution:
            return ["Record study sessions to analyze subject balance."]

        if len(distribution) == 1:
            return ["Record study sessions for at least one more subject to measure balance."]

        recommendations = []
        equal_share = 100 / len(distribution)

        for subject, percentage in distribution.items():
            if percentage < equal_share * 0.5:
                recommendations.append(
                    f"Give more study time to {subject}."
                )

        if self.balance_score() >= 80:
            recommendations.append(
                "Your study time is well distributed across subjects."
            )
        elif not recommendations:
            recommendations.append(
                "Try to distribute study time more evenly."
            )

        return recommendations
