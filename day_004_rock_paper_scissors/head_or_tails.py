import random

for i in range(5):
    random_int = random.randint(0,1)
    if random_int:
        print("head")
    else:
        print("tails")