def get_ai_suggestions(hours, subjects):
    suggestions = []

    if hours < 2:
        suggestions.append("⏱️ Try to increase daily study hours for better results.")
    else:
        suggestions.append("✅ Your daily commitment is great! Keep it consistent.")

    if "Math" in subjects:
        suggestions.append("📊 Practice Math daily to improve problem-solving speed.")

    if "CS" in subjects:
        suggestions.append("💻 Revise data structures and practice coding daily.")

    suggestions.append("🧠 Use the Pomodoro technique for focused learning sessions.")
    suggestions.append("📅 Stick to your schedule and review your plan weekly.")

    return suggestions
