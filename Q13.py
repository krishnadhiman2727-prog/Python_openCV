# Take starting x and y coordinates as input from the user
start_x = int(input("Enter the starting x coordinate: "))
start_y = int(input("Enter the starting y coordinate: "))

# Ask the user for movement direction
direction = input("Enter movement (horizontal or vertical): ").lower()

# Ask the user for the number of steps to move
steps = int(input("Enter the number of steps: "))

current_x = start_x
current_y = start_y

# Check the direction and update coordinates incrementally
if direction == "horizontal":
    for _ in range(steps):
        current_x += 1
        print(f"({current_x}, {current_y})")
elif direction == "vertical":
    for _ in range(steps):
        current_y += 1
        print(f"({current_x}, {current_y})")
else:
    print("Invalid direction. Please enter 'horizontal' or 'vertical'.")