from functions import *


def init():
    athlete_times = []  # this is where the athlete records times will be stored
    number_of_athletes = int(input("How many Athletes are being entered:"))

    if check_number_of_athletes(number_of_athletes):
        # loop thorugh the number of athlets
        for athlete in range(number_of_athletes+1):
            # asks user for gender input. .lower() incase user uses a capital leter
            athlete_gender = input("What gender is the athlete (m|f):").lower()
            athlete_time = int(input("what is the arhletes time:"))

            check_world_record(athlete_time, athlete_gender)
            athlete_times.append(athlete_time)
        print(sorted(athlete_times))

    else:
        print("the number of athletes is not eith the range(4-8)")


if __name__ == "__main__":
    init()
