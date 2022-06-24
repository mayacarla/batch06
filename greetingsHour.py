#Maya Carla Loleatha Anderson
#maya.anderson86@myhunter.cuny.edu
#this program tells the hour of the day given input


hour = int(input("Enter hour (in 24 hour time): "))

if (hour < 12) :
    print("Good Morning")

elif (hour > 12 and hour < 17):
    print("Good Afternoon")

else:
    print("Good Evening")
        
