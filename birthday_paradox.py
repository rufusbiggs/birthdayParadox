import random
from datetime import datetime, timedelta

NUM_SIMULATIONS = 10000

"""
Let's run another 100,000 simulations.
0 simulations run...
10000 simulations run...
--snip--
90000 simulations run...
100000 simulations run.
Out of 100,000 simulations of 23 people, there was a
matching birthday in that group 50955 times. This means
that 23 people have a 50.95 % chance of
having a matching birthday in their group.
That's probably more than you would think!"""

# ignores leap years for simplicity
def generate_birthday():
    random_day_index = random.randint(0,364)
    return datetime(2024,1,1) + timedelta(days = random_day_index)

def generate_birthday_list(num_birthdays):
    return [generate_birthday() for _ in range(num_birthdays)]


def check_for_match(birthday_list):
    birthday_set = set()
    for birthday in birthday_list:
        if birthday in birthday_set:
            return birthday
        birthday_set.add(birthday)
    return False

def format_datetime(date):
    return date.strftime("%d, %b")

def main():
    # Initiate Birthday Paradox Game
    num_birthdays = int(input("How many birthdays should I generate? (max 100)"))

    # Generate and print list of user inputted many birthdays
    if num_birthdays > 100:
        return
    first_birthday_list = generate_birthday_list(num_birthdays)
    formated_birthdays = ', '.join([format_datetime(date) for date in first_birthday_list])
    print(f"Here are {num_birthdays} birthdays: {formated_birthdays}")

    # check for matches in that list
    first_sim_match = check_for_match(first_birthday_list)
    if (first_sim_match):
        print(f"In this simulation, multiple people have a birthday on {format_datetime(first_sim_match)}")
    else:
        print(f"In this simulation, nobody shares a birthday")

    # start simulation 
    print(f"Generating {num_birthdays} random birthdays {NUM_SIMULATIONS} times...")
    input("Press Enter to begin...")
    matches = 0
    for i in range(NUM_SIMULATIONS):
        if i % (NUM_SIMULATIONS / 10) == 0:
            print(f"{i} simulations run...")
        bday_list = generate_birthday_list(num_birthdays)
        if check_for_match(bday_list):
            matches += 1
    print(f"Complete, {NUM_SIMULATIONS} simulations run.")

    # analysis
    print(f"""Out of {NUM_SIMULATIONS} simulations of {num_birthdays} people, there was a
    matching birthday in that group {matches} times. This means
    that {num_birthdays} people have a {round((matches / NUM_SIMULATIONS) * 100, 2)} % chance of
    having a matching birthday in their group.
    That's probably more than you would think!""")
        

if __name__ == "__main__":
    main()
