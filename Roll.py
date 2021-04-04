import random
import time
import os

os.system("cls")

time.sleep(1)

while True:
    minimal = input("Minimal Number: ")
    maximal = input("Maximum Number: ")

    int_min = int(minimal)
    int_max = int(maximal)

    print(random.randint(int_min,int_max))

    time.sleep(3)