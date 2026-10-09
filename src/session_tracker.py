
import json
import os
from datetime import datetime


class StudySessionTracker:

    def __init__(self, file_path="data/sessions.json"):
        self.file_path = file_path
        self.sessions = []
        self.load_sessions()

    def load_sessions(self):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                self.sessions = json.load(file)

    def save_sessions(self):
        with open(self.file_path, "w") as file:
            json.dump(self.sessions, file, indent=4)

    def add_session(self, subject, topic, duration_minutes):
        subject = subject.strip()
        topic = topic.strip()

        if not subject or not topic:
            raise ValueError("Subject and topic cannot be empty.")

        if isinstance(duration_minutes, bool) or not isinstance(
            duration_minutes, (int, float)
        ):
            raise ValueError("Duration must be a positive number.")

        if duration_minutes <= 0:
            raise ValueError("Duration must be greater than zero.")

        session = {
            "id": len(self.sessions) + 1,
            "subject": subject,
            "topic": topic,
            "duration_minutes": duration_minutes,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.sessions.append(session)
        self.save_sessions()

        return session

    def get_sessions(self):
        return self.sessions

    def total_study_minutes(self):
        return sum(
            session["duration_minutes"]
            for session in self.sessions
        )

    def study_time_by_subject(self):
        subject_totals = {}

        for session in self.sessions:
            subject = session["subject"]
            duration = session["duration_minutes"]

            subject_totals[subject] = (
                subject_totals.get(subject, 0) + duration
            )

        return subject_totals
