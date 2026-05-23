from langchain.tools import tool
from database import get_student

@tool
def fetch_student_progress(user_id: str) -> str:
    """
    Fetch a student's learning progress from the database.
    Input: user_id (string)
    Returns a formatted summary of the student's current state.
    """
    student = get_student(user_id)
    if not student:
        return f"No student found with user_id '{user_id}'."

    completed = ", ".join(student["completed_topics"]) or "None"
    pending   = ", ".join(student["pending_topics"])   or "None"

    return (
        f"Student ID    : {student['user_id']}\n"
        f"Goal          : {student['target']}\n"
        f"Current Phase : {student['current_phase']}\n"
        f"Completed     : {completed}\n"
        f"Pending       : {pending}\n"
        f"Study Streak  : {student['streak']} day(s)"
    )


@tool
def suggest_next_topic(user_id: str) -> str:
    """
    Suggest the most appropriate next learning action for a student.
    Input: user_id (string)
    Returns a specific, context-aware recommendation.
    """
    student = get_student(user_id)
    if not student:
        return f"No student found with user_id '{user_id}'."

    pending   = student["pending_topics"]
    completed = student["completed_topics"]
    streak    = student["streak"]
    phase     = student["current_phase"]
    total     = len(pending) + len(completed)

    if not pending:
        suggestion = (
            f"You've completed all topics in '{phase}'! "
            "Consider taking a project challenge to consolidate your skills, "
            "or move on to the next phase."
        )
    elif len(completed) / total >= 0.7:
        suggestion = (
            f"Great progress in '{phase}'! Next recommended topic: "
            f"'{pending[0]}'. After that, consider a mini-project to "
            "apply everything you've learned so far."
        )
    else:
        suggestion = (
            f"Keep going in '{phase}'! Focus on: '{pending[0]}'. "
            f"You have {len(pending)} topic(s) remaining. "
            + (f"Your {streak}-day streak is impressive — keep it up!"
               if streak >= 3 else "Try to study daily to build your streak!")
        )
    return suggestion
