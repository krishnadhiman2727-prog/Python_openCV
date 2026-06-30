# Define the telemetry log string with drone data separated by pipe symbols
telemetry = "DRONE_ID:PX4_001 | ALT:120.5m | SPEED:18.3kmph | BATT:67% | STATUS:HOVERING | GPS:23.0225N,72.5714E"

# Split the telemetry string by '|' to get individual key-value pairs
parts = telemetry.split("|")

# Extract Drone ID
drone_id = parts[0].split(":")[1].strip()

# Extract Altitude, remove the 'm' suffix, and convert to float
altitude = float(parts[1].split(":")[1].replace("m", "").strip())

# Extract Speed, remove the kmph suffix, and convert to float
speed = float(parts[2].split(":")[1].replace("kmph", "").strip())

# Extract Battery percentage, remove the % suffix, and convert to int
battery = int(parts[3].split(":")[1].replace("%", "").strip())

# Extract the status text
status = parts[4].split(":")[1].strip()

# Extract GPS coordinates
gps = parts[5].split(":")[1].strip()

# Check if the status contains "HOVER" (case-insensitive)
contains_hover = "HOVER" in status.upper()
print("Status contains HOVER:", contains_hover)

# Replace HOVERING with RETURNING_HOME in the original telemetry string
updated_telemetry = telemetry.replace("HOVERING", "RETURNING_HOME")
print("Updated telemetry:", updated_telemetry)

# Print a formatted summary using f-strings
print(f"[{drone_id}] Alt: {altitude}m | Batt: {battery}% | Coords: {gps}")