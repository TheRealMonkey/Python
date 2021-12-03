

def init():
    age_in_years = float(input("Enter your age in years:"))
    height_in_cm = float(input("Enter your height in cm:"))
    weight_in_kg = float(input("Enter your wight in kg:"))
    gender = input("enter your gender(m|f)").lower()
    if gender == "m":
        bmr = 88.362 + (13.397 * weight_in_kg) + \
            (4.799 * height_in_cm) - (5.677 * age_in_years)
    else:
        bmr = 447.593 + (9.247 * weight_in_kg) + \
            (3.098 * height_in_cm) - (4.330 * age_in_years)
    bmi = weight_in_kg / ((height_in_cm*100) * (height_in_cm*100))
    exercise_in_week = int(
        input("Enter the number of times you exersice a week:"))

    if exercise_in_week == 0:
        colories_to_maintain = bmr*1.2
    elif exercise_in_week <= 3:
        colories_to_maintain = bmr*1.375
    elif exercise_in_week <= 5:
        colories_to_maintain = bmr*1.55
    elif exercise_in_week <= 7:
        colories_to_maintain = bmr*1.725
    else:
        colories_to_maintain = bmr*1.9
    target_bmi = float(input("Enter the BMI you would like to achieve:"))

    if bmi > target_bmi:
        print(f"you need to decrease your bmi by {bmi-target_bmi}")
    else:
        print(f"you need to increase your bmi by {target_bmi-bmi}")

    print(f"BMI: {bmi}\nBMR:{bmr}")


if __name__ == "__main__":
    init()
    # print(list(str(bmi).split(".")[0]))
