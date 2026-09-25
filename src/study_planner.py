class StudyPlanner:

    def create_plan(self, subject, hours):
        hours = float(hours)

        if hours <= 0:
            return "Study hours must be greater than 0."

        if hours <= 1:
            return f"""
Study Plan for {subject}

1. Read concepts - 20 minutes
2. Make short notes - 15 minutes
3. Practice questions - 20 minutes
4. Quick revision - 5 minutes
"""

        elif hours <= 2:
            return f"""
Study Plan for {subject}

1. Learn concepts - 40 minutes
2. Make notes - 20 minutes
3. Practice questions - 40 minutes
4. Revision - 20 minutes
"""

        else:
            return f"""
Study Plan for {subject}

1. Learn concepts - 60 minutes
2. Make detailed notes - 30 minutes
3. Practice questions - 60 minutes
4. Revision - 30 minutes
5. Take a short break between sessions
"""


def main():
    planner = StudyPlanner()

    subject = input("Enter subject: ")
    hours = input("How many hours can you study? ")

    print(planner.create_plan(subject, hours))


if __name__ == "__main__":
    main()