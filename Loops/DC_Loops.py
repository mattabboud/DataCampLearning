# Initialize offset
offset = 8

# Code the while loop
while offset != 0:
    print("correcting...")
    offset = offset - 1
    print(offset)

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for room in areas:
    print(room)

for index, room in enumerate(areas):
    print("room " + str(index+1) + ": " + str(room))

# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch
for room1, area1 in house:
    print("the " + room1 + " is " + str(area1) + " sqm")
