import pandas as pd


class StudyDataPreprocessor:

    REQUIRED_COLUMNS = [
        "id",
        "subject",
        "topic",
        "duration_minutes",
        "date"
    ]

    def preprocess_sessions(self, sessions):
        """Clean study-session records and return a DataFrame."""
        if not sessions:
            return pd.DataFrame(columns=self.REQUIRED_COLUMNS)

        df = pd.DataFrame(sessions)

        # Ensure required columns exist.
        for column in self.REQUIRED_COLUMNS:
            if column not in df.columns:
                df[column] = pd.NA

        df = df[self.REQUIRED_COLUMNS].copy()

        # Clean text fields.
        for column in ["subject", "topic"]:
            df[column] = df[column].astype("string").str.strip()
            df[column] = df[column].replace("", pd.NA)

        # Convert numeric fields safely.
        df["id"] = pd.to_numeric(df["id"], errors="coerce")
        df["duration_minutes"] = pd.to_numeric(
            df["duration_minutes"], errors="coerce"
        )

        # Parse dates safely.
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

        # Remove records missing essential information.
        df = df.dropna(
            subset=["id", "subject", "topic", "duration_minutes", "date"]
        )

        # Exclude invalid durations and IDs.
        df = df[
            (df["id"] > 0) &
            (df["duration_minutes"] > 0)
        ].copy()

        # Remove duplicate session IDs.
        df = df.drop_duplicates(subset=["id"], keep="first")

        return df.reset_index(drop=True)
