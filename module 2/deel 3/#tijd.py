#tijd

time = 1

while time <= 24:
    if time < 12:
        print(f"{time} AM")
    else:
        adjusted_time = time - 12
        print(f"{adjusted_time} PM")

    time += 1
