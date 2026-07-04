print("CLOCK PROGRAM:")

name = input("enter your name: ")
print("welcome", name, "to the clock program! let's check the current time and greet you accordingly!")

import time

clock = time.strftime("%H:%M:%S")
if(clock >= "00:00:00" and clock < "12:00:00"):
    print("Good Morning! The current time is:", clock)
elif(clock >= "12:00:00" and clock < "18:00:00"):
    print("Good Afternoon! The current time is:", clock)
else:
    print("Good Evening! The current time is:", clock)

print("thank you for using our clock program, have a nice day ahead!")