def check_goal_status(current_calories, goal):
    if current_calories >= goal:
        return f"🎉 Congratulations! You achieved your goal of {goal} calories!"
    else:
        remaining = goal - current_calories
        return f"💡 You need {remaining:.2f} more calories to reach your goal."
