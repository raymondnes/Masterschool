def age_in_seconds(age):
    days_in_a_year = 365.25
    seconds_in_a_day = 24 * 60 * 60
    current_age = age
    total_seconds = days_in_a_year * seconds_in_a_day * current_age
    print(total_seconds)

age_in_seconds(1)
