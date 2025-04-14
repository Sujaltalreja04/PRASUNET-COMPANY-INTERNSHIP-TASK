import streamlit as st
import requests
from datetime import datetime, timedelta
import json
import os

st.set_page_config(page_title='🧠 AI Study Planner', layout='centered')
st.title("📚 AI-Based Study Planner")

# Dummy user data storage
USER_DATA_DIR = "user_data"
if not os.path.exists(USER_DATA_DIR):
    os.makedirs(USER_DATA_DIR)

def get_ai_suggestions_with_llm(subjects, hours):
    prompt = f"""
    I am preparing for exams. I have the following subjects: {', '.join(subjects)}.
    I can study {hours} hours per day. Suggest some effective study techniques,
    tips, and motivation strategies personalized for these subjects and time limit.
    """
    try:
        response = requests.post("http://localhost:11434/api/generate", json={
            "model": "tinyllama",
            "prompt": prompt,
            "stream": False
        })
        return response.json()["response"].strip().split("\n")
    except Exception as e:
        return [f"⚠️ Could not fetch suggestions: {e}"]

def authenticate_user(username, password):
    # Dummy authentication function
    return username == "user" and password == "pass"

def save_user_plan(username, plan):
    with open(os.path.join(USER_DATA_DIR, f"{username}_plan.json"), "w") as f:
        json.dump(plan, f)

def load_user_plan(username):
    try:
        with open(os.path.join(USER_DATA_DIR, f"{username}_plan.json"), "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def delete_user_plan(username):
    try:
        os.remove(os.path.join(USER_DATA_DIR, f"{username}_plan.json"))
    except FileNotFoundError:
        pass

def send_notification(username, message):
    # Dummy notification function
    st.sidebar.info(f"Notification for {username}: {message}")

def get_study_analytics(plan):
    # Dummy analytics function
    total_hours = sum(sum(schedule.values()) for schedule in plan.values())
    return {"total_study_hours": total_hours}

def generate_study_plan(subjects, hours, start_date, end_date):
    plan = {}
    current_date = start_date
    while current_date <= end_date:
        schedule = {subject: hours // len(subjects) for subject in subjects}
        plan[current_date.strftime("%Y-%m-%d")] = schedule
        current_date += timedelta(days=1)
    return plan

st.sidebar.title("User Authentication")
username = st.sidebar.text_input("Enter your name").strip()
password = st.sidebar.text_input("Enter your password", type="password").strip()

if st.sidebar.button("Login"):
    if authenticate_user(username, password):
        st.sidebar.success("Login successful!")
        st.session_state.authenticated = True
    else:
        st.sidebar.error("Invalid credentials")

if st.session_state.get("authenticated", False):
    existing_plan = load_user_plan(username)
    if existing_plan:
        st.success("📂 Loaded previous study plan!")
        if st.checkbox("Show previous plan"):
            for date, sched in existing_plan.items():
                st.markdown(f"**{date}**")
                st.json(sched)

    st.header("🔧 Build Your New Plan")

    subjects = st.multiselect("Select your subjects", ["Math", "Science", "English", "History", "CS", "Geography", "Economics"])
    hours = st.slider("How many hours can you study per day?", 1, 10)
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")

    if st.button("📅 Generate Plan"):
        if not username or not subjects or start_date >= end_date:
            st.error("❌ Please enter all valid inputs!")
        else:
            plan = generate_study_plan(subjects, hours, start_date, end_date)
            save_user_plan(username, plan)
            st.success("✅ New study plan saved!")

            st.subheader("📆 Your Study Plan:")
            for date, schedule in plan.items():
                st.markdown(f"### {date}")
                for subject, hour in schedule.items():
                    st.write(f"📘 {subject}: {hour} hrs")

            st.subheader("💡 AI Suggestions")
            tips = get_ai_suggestions_with_llm(subjects, hours)
            for tip in tips:
                st.info(tip)

            st.subheader("📊 Study Analytics")
            analytics = get_study_analytics(plan)
            st.json(analytics)

            st.subheader("🔔 Notifications")
            if st.button("Send Notification"):
                send_notification(username, "Your study plan has been generated!")
                st.success("Notification sent!")

    if st.button("🗑️ Clear Old Plan"):
        delete_user_plan(username)
        st.warning("Old plan deleted.")

    st.sidebar.title("Sync with Calendar")
    if st.sidebar.button("Sync with Google Calendar"):
        st.sidebar.info("Feature coming soon!")

else:
    st.warning("Please login to access the study planner.")
