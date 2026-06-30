# Define waypoints as a tuple of tuples (immutable)
waypoints = (
    ("WP1", 23.0225, 72.5714, 50),
    ("WP2", 23.0312, 72.5801, 80),
    ("WP3", 23.0401, 72.5900, 100),
    ("WP4", 23.0225, 72.5714, 0),
)

# Print the total number of waypoints using the len() function
print("Total number of waypoints:", len(waypoints))

# Use tuple unpacking to print each waypoint's details in a formatted line
for name, lat, lon, alt in waypoints:
    print(f"{name}--Lat: {lat} degree, Lon: {lon} degree, Alt: {alt}m")

# Find the waypoint with the highest altitude using a loop
highest_waypoint = waypoints[0]  # Initialize with the first waypoint
for wp in waypoints:
    # Compare the altitude (index 3) of each waypoint
    if wp[3] > highest_waypoint[3]:
        highest_waypoint = wp
print("Waypoint with highest altitude:", highest_waypoint)

# Check if a specific waypoint exists in the tuple
target = ("WP2", 23.0312, 72.5801, 80)
exists = target in waypoints
print("Target waypoint exists:", exists)

# Try to modify WP1's altitude and catch the TypeError (tuples are immutable)
try:
    waypoints[0] = ("WP1", 23.0225, 72.5714, 60)
except TypeError as e:
    print("Waypoint data is immutable mission integrity protected!")