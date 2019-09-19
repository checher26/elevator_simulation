import random
import time
import matplotlib.pyplot as plt
import numpy as np

from turtle import *

maxX = 400
maxY = 900
canvas = Screen()
canvas.setup(maxX, maxY)
canvas.bgcolor("blue")
elevator = Turtle()
elevator.hideturtle()
elevator.pensize(width=4)

floors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
activities = ["lobby", "pool", "diningHall", "gym", "theater", "recCenter", "spa", "rooms1", "rooms2", "rooms3"]

floors_activities = list(zip(floors, activities))
floors_activities_dict = dict(floors_activities)     #links floor with activity
print(floors_activities_dict)

numOfTrials = 2
numPeople = 5
startAsciiVal = 65
maxFloors = 10
startFloor = 2
endFloor = maxFloors
UpDownFlag = "Up"
floorStats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
personList = []
personListSorted = []


class person():
    numPersons = 0

    def __init__(self, name, floor):                 #creates a class
        person.numPersons += 1
        self.name = name
        self.floor = floor


def createPersonList(startAsciiVal):
    person.numPersons = 0
    for i in range(numPeople):
        personList.append(person(chr(startAsciiVal), random.randint(startFloor, endFloor)))       #creates a list with names and random detination floors
        startAsciiVal += 1
    for j in range(numPeople):
        print(personList[j].name, personList[j].floor)
    return startAsciiVal


def sortList():
    print("Sorted List:")
    # sort in ascending order
    if UpDownFlag == "Up":

        for j in range(len(personList)):
            min = personList[0]
            for i in range(len(personList)):
                if min.floor > personList[i].floor:           # when elevator is going up, sorts list in ascending order by finding minimum each time and appending into sorted list
                    min = personList[i]

            personListSorted.append(min)
            personList.remove(min)

        for j in range(len(personListSorted)):
            print(personListSorted[j].name, personListSorted[j].floor)
    else:
        # sort in descending order
        for j in range(len(personList)):
            max = personList[0]
            for i in range(len(personList)):
                if max.floor < personList[i].floor:          # when elevator is going down, sorts list in descending order by finding maximum each time and appending into sorted list
                    max = personList[i]
            personListSorted.append(max)
            personList.remove(max)
        for j in range(len(personListSorted)):
            print(personListSorted[j].name, personListSorted[j].floor)


def drawLine(UpDownFlag):              #https://docs.python.org/2/library/turtle.html
    elevator.pensize(width=4)
    elevator.penup()
    if UpDownFlag=="Up":
        elevator.goto(0, -maxY / 2)    #pen goes to (0,-450)
        elevator.pendown()             #lines are visibile when pendown or pen is down
        elevator.left(90)
        elevator.forward(maxY)         #draws line from bottom to top
        elevator.penup()               #lines don't show when penup or pen is up
        elevator.goto(0, -maxY / 2)
    else:
        elevator.goto(0, maxY / 2)     #pen goes to (0,450)
        elevator.pendown()
        elevator.right(90)             #rotates 90 degrees
        elevator.forward(maxY)         #draws line from top to bottom
        elevator.penup()
        elevator.goto(0, maxY / 2)

def drawsquare():
    elevator.pendown()                # square will be drawn at that floor
    elevator.pensize(width=8)
    elevator.color("black", "red")
    elevator.begin_fill()             #makes inside of square red

    elevator.right(90)                #will outline the square by rotating 90 degress and moving forward 50
    elevator.forward(50)
    elevator.left(90)
    elevator.forward(50)
    elevator.left(90)
    elevator.forward(50)
    elevator.left(90)
    elevator.end_fill()


def insertPerson(currentFloor, personListSorted, UpDownFlag, startAsciiVal):          #new person gets on the elevator
    if (currentFloor + 1) < 10 and UpDownFlag == "Up":
        name = chr(startAsciiVal)
        startAsciiVal += 1                                                            #A person can get into elevator only at the floor the elevator stops
        newPerson = person(name, random.randint((currentFloor + 1), maxFloors))       #destination floor has to be higher than current floor
        x = newPerson.floor
        print("new person name ", newPerson.name,"floor", x)

        i = 0
        point = 0
        ListLastElement = len(personListSorted) - 1
        # if list is empty insert as the first element
        if len(personListSorted) == 0:
            point = 0
        # insert as the last element in the list if the new floor is greater than the current last element in the list
        elif x > personListSorted[ListLastElement].floor:
            point = len(personListSorted)
        else:
            # find the postion to insert by checking if greater than and less than
            while i < len(personListSorted) - 1:
                if personListSorted[i].floor <= x and x <= personListSorted[i + 1].floor:
                    point = i + 1
                i += 1
        personListSorted.insert(point, newPerson)          #inserts both name and floor into personListSorted by inserting newPerson at a specific point


    elif currentFloor > 1 and UpDownFlag == "Down":                          #new person gets on the elevator
        name = chr(startAsciiVal)
        startAsciiVal += 1
        newPerson = person(name, random.randint(1, currentFloor - 1))        #destination floor has to be lower than current floor
        x = newPerson.floor
        print("new person name ", newPerson.name, "going to floor", x)
        i = 0
        point = 0
        ListLastElement = len(personListSorted) - 1
        # if list is empty insert as the first element
        if len(personListSorted) == 0:
            point = 0
            # insert as the last element in the list if the new floor is less than the current last element in the list
        elif x < personListSorted[ListLastElement].floor:
            point = len(personListSorted)
        else:
            # find the postion to insert by checking if greater than and less than
            while i < len(personListSorted) - 1:
                if personListSorted[i].floor >= x and x >= personListSorted[i + 1].floor:
                    point = i + 1
                i += 1
        personListSorted.insert(point, newPerson)            #inserts both name and floor into personListSorted by inserting newPerson at a specific point
    return startAsciiVal


# def reset(personList, personListSorted):
#     personList = []
#     personListSorted = []


for trial in range(numOfTrials):
    print("elevator is going ", UpDownFlag)            #UpDownFlag is direction elevator is going in

    startAsciiVal = createPersonList(startAsciiVal)    #starts ascii value at 65 and goes up by 1 for each person added to the list
    sortList()

    while (len(personListSorted)) > 0:
                                                       #elevator starts from ground floor and stops at the floors in personListSorted
        val = personListSorted[0]                      #val becomes the first element(both name and floor)
        currentFloor = val.floor
        print("elevator is on floor ", currentFloor)
        j = 0
        i = 0
                                                                          # to remove all the occurences of the same floor
        while val.floor == currentFloor and len(personListSorted) > 0:
            val = personListSorted[i]
            if val.floor == currentFloor:
                personListSorted.remove(val)
                j += 1                          #represents how many times a floor is in the list



        print("Number of people coming out is", j)
        floorStats[currentFloor - 1] += j       #floors start at 1 but indexing starts at 0 so have to do currentFloor - 1

        # Turtle section

        drawLine(UpDownFlag)                                            #https://docs.python.org/2/library/turtle.html
        if UpDownFlag == "Up":
            elevator.goto(0, (-maxY / 2 + currentFloor * 65))           #draws the elevator at specific spot based on floor
        else:
            elevator.goto(0, (315 - (11-currentFloor)*65))
        elevator.write(currentFloor, font=("Arial", 16, "normal"))      #displays the floor in the square

        drawsquare()
        canvas.delay(5)                    #time it takes to draw
        elevator.clear()
        elevator = Turtle()
        elevator.hideturtle()              #so icon drawing the lines doesn't show




        # takes in new people at the floor it stopped but have to make sure that the people select the floors greater than the current floor where the elevator is
        startAsciiVal = insertPerson(currentFloor, personListSorted, UpDownFlag, startAsciiVal)

    if UpDownFlag == "Up":
        UpDownFlag = "Down"
        startAsciiVal = 65
        startFloor = 1          #when going down, won't select 10 because it starts at floor 10
        endFloor = 9

    else:                        # Elevator starts at the 1st floor when going up
                                 # Elevator starts at the 10th floor when coming down
        UpDownFlag = "Up"
        startAsciiVal = 65
        startFloor = 2         #when going up, won't select 1 because it starts at floor 1
        endFloor = 10
    #reset(personList, personListSorted)

print(floorStats)

maxVal = floorStats[0]
pFloor = 1
for i in range(len(floorStats)):          # finds the floor that's most visited, floor 1 is at index 0
    if maxVal < floorStats[i]:           #compares all values to find greatest value
        maxVal = floorStats[i]
        pFloor = i + 1                #actual floor will be the index plus 1 since indexing starts at 0

print("The most popular floor is", pFloor,"," ,floors_activities_dict[pFloor], "on this floor")     #dict[pFloor] uses key to get the activity for that floor

y_pos = np.arange(len(activities))
plt.barh(y_pos, floorStats, align='center', alpha=0.5)      #barh makes the graph horizontal https://pythonspot.com/en/matplotlib-bar-chart/
plt.yticks(y_pos, activities)
plt.xlabel("Number of Times Visited")
plt.ylabel("Name of Floor")
plt.title('Popular Floors')
plt.show()


# Elevator keeps going in the same direction until the last person gets off in one direction, before changing direction
# for example if an elevator is going up, it won't stop to pick up passengers who want to go down until it's done with everything that requires it to go up.
# If nobody wants to go further up, the elevator turns around.

#References:
#https://docs.python.org/2/library/turtle.html
#https://pythonspot.com/en/matplotlib-bar-chart/