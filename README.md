
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
│   └── tasks.json
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
│   └── progress.py
│
└── tests/
Author 
Arpita Nayak


## Day 19 Update

Added persistent study session tracking and study-time analytics, including totals by subject.
