def get_achievements(total_calories):
    achievements = []
    if total_calories >= 500:
        achievements.append("🏅 First 500 Calories Burned!")
    if total_calories >= 1000:
        achievements.append("🔥 1,000 Calories Master!")
    if total_calories >= 5000:
        achievements.append("💪 Fitness Pro: 5,000 Calories Burned!")
    return achievements
