from functions import *


def check_world_record(time, gender):
    """this will check if the time is higher then the world record

    Args:
        time (float): the time that needs to be checked
        gender (int): male= 0|female= 1
    """
    record = {"m": {
        "World": 9.58,
        "Europian": 9.86,
        "British": 9.87


    }, "f": {
        "World": 10.49,
        "Europian": 10.73,
        "British": 10.99


    }}
    for key in record[gender]:
        if time > record[gender][key]:
            print(f"the {key} record has been beaten!")


def check_number_of_athletes(number_of_athletes):
    """checks if the number of athletes is between 4 and 8

    Args:
        athletes (int): number of athletes

    Returns:
        boolean: will return true if number of athletes is within range
    """

    if number_of_athletes >= 4 and number_of_athletes <= 8:
        return number_of_athletes
    else:
        return False


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
