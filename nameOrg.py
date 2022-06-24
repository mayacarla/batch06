#Maya Carla Loletha Anderson

names = input("Please enter your list of names:")

myNames = names.split(";")

print("You entered:")
      
for name in myNames:
    noComma = name.split(",")
    print(noComma[1], noComma[0])

print("Thank you for using my name organizer!")
