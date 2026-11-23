def vacuum_agent(location, rooms):
    print("Current Location:", location)

    if rooms[location] == 1:
        print("Room is Dirty. Cleaning...")
        rooms[location] = 0
    else:
        print("Room is Clean.")

    
    if location == 'A':
        location = 'B'
    else:
        location = 'A'

    return location



rooms = {
    'A': 1,
    'B': 1
}

location = 'A'


while 1 in rooms.values():
    location = vacuum_agent(location, rooms)

print("\nAll rooms are clean!")
print("Final Room Status:", rooms)
