
# StudyMate AI

StudyMate AI is a study management and learning assistant developed as part of a 45-day Artificial Intelligence and Generative AI internship project.

The project is being developed progressively, with new features, analysis techniques, and AI/ML capabilities planned throughout the internship.

## Problem Statement

Students often manage their notes, study tasks, and progress using separate tools. This can make it difficult to organize study material, track tasks, analyze learning activity, and identify areas that need improvement.

StudyMate AI aims to bring these activities together into one study assistant application.

## Objectives

- Manage and organize study notes.
- Create and track study tasks.
- Generate simple study plans.
- Analyze study-related text.
- Extract meaningful keywords from notes.
- Analyze notes using structured data.
- Visualize study and note-related information.
- Track study task completion.
- Gradually introduce Machine Learning, AI, and Generative AI capabilities.
- Develop a practical real-world study assistance application.

## Current Features

### Note Management
- Add study notes.
- View saved notes.
- Search notes using keywords.
- Delete notes.
- Store notes using JSON persistence.

### Study Task Management
- Add study tasks.
- View study tasks.
- Mark tasks as completed.
- Store tasks using JSON persistence.

### Study Planner
- Generate a basic study plan based on the subject and available study time.

### Text Processing
- Word counting.
- Character counting.
- Stop-word removal.
- Common meaningful word detection.
- Keyword extraction.
- Reading-time estimation.

### Note Analytics
- Total number of notes.
- Notes grouped by subject.
- Notes grouped by topic.
- Pandas-based data analysis.

### Data Visualization
- Notes by subject visualization.
- Notes by topic visualization.
- Study task completion visualization.
- Completed vs pending task analysis.

### Study Session Tracking
- Record study sessions by subject and topic.
- Store study duration and timestamp.
- View recorded sessions.
- Calculate total study time.
- Analyze study time by subject.
- Persist sessions using JSON storage.

### Study Progress
- Total tasks.
- Completed tasks.
- Pending tasks.
- Task completion percentage.
- Visual progress representation.

## Technologies Used

- Python
- JSON
- Pandas
- Matplotlib
- NumPy

Additional Machine Learning, AI, and Generative AI technologies will be introduced in later stages of development.

## Project Structure

```text
StudyMate-AI/
│
├── app.py
├── README.md
├── requirements.txt
│
├── data/
│   ├── notes.json
│   ├── tasks.json
│   └── sessions.json
│
├── models/
│
├── src/
│   ├── __init__.py
│   ├── notes.py
│   ├── task_manager.py
│   ├── study_planner.py
│   ├── text_processor.py
│   ├── analytics.py
│   ├── visualizer.py
│   ├── progress.py
│   ├── session_tracker.py
│   ├── data_preprocessor.py
│   ├── study_analytics.py
│   └── weekly_analytics.py
│
└── tests/
Author 
Arpita Nayak


## Day 19 Update

Added persistent study session tracking and study-time analytics, including totals by subject.

## Day 20 Update — Study-Time Visualization

- Added visualization of study time by subject.
- Used Matplotlib to display study-time comparisons.

## Day 21 Update — Study Data Preprocessing

- Convert study-session records into a Pandas DataFrame.
- Clean whitespace from subject and topic fields.
- Convert duration and date columns to appropriate data types.
- Handle missing values and invalid dates.
- Remove duplicate session IDs and invalid durations.
- Preserve the original JSON data during preprocessing.

## Day 22 Update — Study Session Analytics

- Calculate total study time and number of sessions.
- Calculate average session duration.
- Summarize study time by subject.
- Identify the most-studied subject.
- Handle empty datasets safely.

## Day 23 Update — Daily Study Goal Tracking

- Set and persist a daily study-time goal.
- Calculate today's study time from recorded sessions.
- Display remaining study time and goal completion percentage.
- Identify when the daily goal has been achieved.
- Validate goal values and handle days without study sessions.
- Integrate Study Goals into the main application menu.

## Day 24 Update — Weekly Study Analytics

- Summarize study time for each day from Monday to Sunday.
- Calculate total study time for the current week.
- Calculate average daily study time across the week.
- Identify the most productive day.
- Handle empty datasets and invalid study-session records safely.
- Integrate Weekly Analytics into the main application menu.
### day 25

## Day 25 Update — Weekly Study-Time Visualization

- Added a weekly study-time bar chart using Matplotlib.
- Displayed daily study minutes from Monday through Sunday.
- Handled weeks with no recorded study time.
- Tested the chart with sample data and existing weekly analytics.

## Day 26 Update — Daily Study Goal Comparison

- Added a chart comparing the daily study goal with actual study time.
- Reused the existing StudyGoalTracker to load the saved goal and today's study duration.
- Added validation for non-positive goals and negative study time.
- Tested the chart with real tracker data and sample values.


## Day 27 Update — Monthly Study Analytics

- Added a monthly study analytics module in `src/monthly_analytics.py`.
- Calculate total study minutes and the number of sessions for a selected month.
- Calculate average study-session duration.
- Group monthly study time by subject.
- Identify the most-studied subject for the selected month.
- Filter records by both month and year.
- Handle empty datasets, invalid dates, and non-positive durations.
- Tested the module with sample data and edge cases.
