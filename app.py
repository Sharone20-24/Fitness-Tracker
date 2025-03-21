import streamlit as st
import joblib
import pandas as pd
import plotly.express as px
from utils.recommendations import get_recommendations
from utils.achievements import get_achievements
from utils.goals import check_goal_status

# Load models
classifier = joblib.load(r'C:\\Users\\Sharone\\Documents\\fitness-tracker[1]\\fitness-tracker\\models\\classifier.pkl')
regressor = joblib.load(r'C:\\Users\\Sharone\\Documents\\fitness-tracker[1]\\fitness-tracker\\models\\regressor.pkl')

# Streamlit Configuration
st.set_page_config(page_title="🔥 Advanced Fitness Tracker", layout="wide")

# Sidebar - User Input with Sliders
st.sidebar.title("🏃‍♂️ Fitness Tracker Input")
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
age = st.sidebar.slider("Age", 10, 80, 25)
height = st.sidebar.slider("Height (cm)", min_value=100, max_value=250, value=170)
weight = st.sidebar.slider("Weight (kg)", min_value=30, max_value=200, value=70)
duration = st.sidebar.slider("Workout Duration (minutes)", 5, 120, 30)
heart_rate = st.sidebar.slider("Heart Rate (bpm)", 60, 200, 100)
body_temp = st.sidebar.slider("Body Temperature (°C)", min_value=35.0, max_value=42.0, value=37.0)

# Set personal goal with a slider
goal = st.sidebar.slider("🎯 Set Your Calorie Goal", min_value=100, max_value=5000, value=2000)

# Main Section
st.title("🔥 **Advanced Fitness Tracker Dashboard**")
st.markdown("Track your workouts, visualize your progress, and hit your fitness goals! 💪")

# Predict button
if st.sidebar.button("📊 Predict & Analyze"):
    input_data = pd.DataFrame({
        'Gender': [0 if gender == 'Male' else 1],
        'Age': [age],
        'Height': [height],
        'Weight': [weight],
        'Duration': [duration],
        'Heart_Rate': [heart_rate],
        'Body_Temp': [body_temp]
    })

    # Predictions
    classification_result = classifier.predict(input_data)[0]
    calorie_prediction = regressor.predict(input_data)[0]

    # Display results
    st.subheader("🔍 Prediction Results")
    if classification_result:
        st.success("🔥 High Calorie Burn Achieved!")
    else:
        st.info("💡 Lower Calorie Burn Recorded.")

    st.metric("🔥 Estimated Calories Burned", f"{calorie_prediction:.2f} kcal")

    # Achievements
    st.subheader("🏆 Achievements")
    achievements = get_achievements(calorie_prediction)
    if achievements:
        for badge in achievements:
            st.success(badge)
    else:
        st.info("Keep going to unlock achievements! 💪")

    # Goal Tracker
    st.subheader("🎯 Goal Progress")
    goal_status = check_goal_status(calorie_prediction, goal)
    st.info(goal_status)

    # Personalized Recommendations
    st.subheader("💡 Personalized Recommendations")
    recs = get_recommendations(gender, age, duration, heart_rate)
    for rec in recs:
        st.write(rec)

    # Progress Chart (Dummy Data for Visualization)
    st.subheader("📈 Weekly Calorie Burn Progress")
    progress_data = {
        'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        'Calories': [300, 450, 500, 400, 600, 700, calorie_prediction]
    }
    df_progress = pd.DataFrame(progress_data)
    fig = px.line(df_progress, x='Day', y='Calories', title='Weekly Progress 🔥', markers=True)
    st.plotly_chart(fig)

# Footer
st.markdown("---")
st.caption("Made with ❤️ by Your Fitness App - Stay Strong 💪")
