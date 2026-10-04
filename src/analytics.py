import pandas as pd


class NoteAnalytics:

    def __init__(self, notes):
        self.notes = notes

    def create_dataframe(self):
        if not self.notes:
            return pd.DataFrame(
                columns=["id", "subject", "topic", "content"]
            )

        return pd.DataFrame(self.notes)

    def total_notes(self):
        return len(self.notes)

    def notes_by_subject(self):
        df = self.create_dataframe()

        if df.empty:
            return {}

        return df["subject"].value_counts().to_dict()

    def notes_by_topic(self):
        df = self.create_dataframe()

        if df.empty:
            return {}

        return df["topic"].value_counts().to_dict()
    