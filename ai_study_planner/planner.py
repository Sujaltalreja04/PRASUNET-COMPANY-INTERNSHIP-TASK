from datetime import timedelta

def generate_study_plan(subjects, daily_hours, start_date, end_date):
    plan = {}
    total_days = (end_date - start_date).days + 1
    hours_per_subject = daily_hours / len(subjects)

    for i in range(total_days):
        day = start_date + timedelta(days=i)
        date_str = day.strftime("%Y-%m-%d")
        plan[date_str] = {}

        for subject in subjects:
            plan[date_str][subject] = round(hours_per_subject, 2)

    return plan
