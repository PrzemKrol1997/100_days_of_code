from datetime import datetime


day = (input("what day is it?(if empty = today): "))
if day == "":
    day = datetime.now().strftime("%d.%m")

distance_run = input("how far have you run?: ")
dumbbell_shoulder_press = input("how many dumbbell shoulder press have you make? ")
sit_ups = input("how many sit ups?: ")
plank = input("how long did you do plank?: ")

new_data = {'day': day, 'distance run': distance_run,
            "dumbbell shoulder press": dumbbell_shoulder_press,
            "sit-ups":sit_ups,
            "plank":plank}

try:
    with open("training.txt", "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    lines = []

new_row = f"{new_data['day']:<10} {new_data['distance run']:<15} {new_data['dumbbell shoulder press']:<25} {new_data['sit-ups']:<10} {new_data['plank']:<10}\n"

with open("training.txt", "a") as file:
    if not lines:
        file.write (f"{'day':<10} {'distance run':<15} {'dumbbell shoulder press':<25} {'sit-ups':<10} {'plank':<10}\n")
    file.write(new_row)