# 🚦 Traffic Light Script
# This was my first program using if-elif-else logic in Python.
# It takes user input and prints a message based on the color.


light = input("Enter light color (Red / Yellow / Green: ")

if (light == "green"):
    print("Go")
elif (light == "Yellow"):
     print("Start")
elif (light == "Red" ):
     print("Stop")
else:
     print("light is Broken")
     
