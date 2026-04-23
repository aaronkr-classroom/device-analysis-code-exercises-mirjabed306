from room_sensor import RoomSensor

# Part 3: Create objects
sensor1 = RoomSensor("Kitchen", 31, 72, 180)
sensor2 = RoomSensor("Bedroom", 24, 50, 300)
sensor3 = RoomSensor("Balcony", 27, 65, 150)

# Store in list
sensors = [sensor1, sensor2, sensor3]

# Part 5: Counters
comfortable = 0
normal = 0
warning = 0

# Part 4: Loop through list
for s in sensors:
    s.show_info()

    level = s.comfort_level()
    light = s.light_status()

    print("Comfort Level:", level)
    print("Light Status:", light)
    print()

    # Counting categories
    if level == "Comfortable":
        comfortable += 1
    elif level == "Normal":
        normal += 1
    else:
        warning += 1

# Final result
print("Comfortable:", comfortable)
print("Normal:", normal)
print("Warning:", warning)