import random
import time
import os



time.sleep(1)

while True:
    os.system("cls")
    
    minimal = input("Minimal Number: ")
    maximal = input("Maximum Number: ")

    int_min = int(minimal)
    int_max = int(maximal)

    print(random.randint(int_min,int_max))

    time.sleep(3)