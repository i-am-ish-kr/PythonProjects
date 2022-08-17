from ast import Break, main
import imp
from time import *
import random as rn

def mistake(paratest, usertest):
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error


def speed_test(time_s, time_e, userinput):
    time_diff = time_e - time_s
    time_r = round(time_diff, 2)
    speed = len(userinput)/ time_r
    return round(speed)

if __name__ == '__main__':
    while True:
        check = input(" Ready for test : Yes/No : ")
        if check == "Yes":

            test = ["this is a typing speed calculator and we are using python3 here", 
                    "My name is Amish Kumar and I am a teacher at Skillsahre." "This is Python Project Course and it is full of fun."]

            test1  = rn.choice(test)

            print("   ******************Typing Speed Calculator******************")
            print()
            print(test1)
            print()
            print()
            time_1 = time()
            testinput = input(" Enter: ")
            time_2 = time()
        
            print("Speed: ", speed_test(time_1, time_2, testinput), " w/sec")
            print("Error: ", mistake(test1, testinput))
        elif check == "No":
            print("Thank You")
            break

        else:
            print("Wrong Input")

