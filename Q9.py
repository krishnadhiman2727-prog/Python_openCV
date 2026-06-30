# Define the current drone state as a dictionary
drone_state = {
    "battery": 18,
    "altitude": 95,
    "signal_strength": 40,
    "distance_from_home": 850,
    "wind_speed": 38,
    "obstacle_detected": True
}

# Check all RTH trigger rules independently using if statements
print("RTH Trigger Checks:")
if drone_state["battery"] < 20:
    print("CRITICAL: RTH triggered - Low Battery")

if drone_state["signal_strength"] < 30:
    print("WARNING: RTH triggered - Signal Lost")

if drone_state["wind_speed"] > 35:
    print("WARNING: RTH triggered - High Wind")

if drone_state["obstacle_detected"] is True:
    print("CAUTION: Obstacle detected - Rerouting")

if (drone_state["battery"] >= 20 and 
    drone_state["signal_strength"] >= 30 and 
    drone_state["wind_speed"] <= 35 and 
    not drone_state["obstacle_detected"]):
    print("All systems nominal")

# Simulate descent from current altitude to 0 in steps of 15m
print("\nSimulated Descent:")
current_altitude = drone_state["altitude"]
current_battery = drone_state["battery"]

while current_altitude > 0:
    print(f"Altitude: {current_altitude}m | Battery: {current_battery}%")
    current_altitude -= 15
    if current_altitude < 0:
        current_altitude = 0
    current_battery -= 1

# Print final state after landing
print(f"Altitude: {current_altitude}m | Battery: {current_battery}%")
print("Drone has landed successfully")