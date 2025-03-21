def get_recommendations(gender, age, duration, heart_rate):
    recommendations = []

    # Gender-specific advice
    if gender.lower() == 'male':
        recommendations.append("🏋️ Try strength training for muscle gain.")
    else:
        recommendations.append("🧘 Yoga or Pilates can help with flexibility and relaxation.")

    # Age-based advice
    if age < 30:
        recommendations.append("🔥 Increase your workout intensity for better endurance.")
    else:
        recommendations.append("🚶 Focus on low-impact exercises like walking or swimming.")

    # Duration-based
    if duration < 30:
        recommendations.append("⏳ Try to work out for at least 30 minutes a day.")
    else:
        recommendations.append("👍 Great job maintaining a healthy workout duration!")

    # Heart rate advice
    if heart_rate > 140:
        recommendations.append("💓 Monitor your heart rate, and take breaks if needed.")
    else:
        recommendations.append("💪 Keep up the good pace!")

    return recommendations
