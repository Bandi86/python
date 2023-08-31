import random
import time

min = 1
max = 6

max_input = input("Hány oldalú legyen a dobókocka? (alapértelmezett = 6) ")

if max_input != "" and max_input.isnumeric():
    max = int(max_input)

#véletlen szám generálása
def dice_throw():
    return random.randint(min,max)

#loading
def loading():
    print("Dobókocka eldobása:")
    time.sleep(0.5)

while True:
    answer = input("Eldobjuk e a kockát? [i/n]")
    
    if answer == "i":
        print(dice_throw())
    
    elif answer == "n":
        print("Viszlát")
        break
    else:
        print("Invalid Input [i/n]")