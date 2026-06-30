# Define drone specifications
max_takeoff_weight = 4.5    # Maximum allowed takeoff weight in kg (float)
frame_weight = 1.2          # Weight of the drone frame in kg (float)
battery_weight = 0.8        # Weight of the battery in kg (float)
num_propellers = 4          # Number of propellers on the drone (int)
motor_weight = 0.075        # Weight of each motor in kg (float)
is_gps_enabled = True       # GPS availability (bool)
gps_module_weight = 0.05    # Weight of the GPS module in kg (float)

# Calculate the maximum payload the drone can carry
# Formula: max payload = max takeoff weight - all component weights
max_payload = max_takeoff_weight - frame_weight - battery_weight - (num_propellers * motor_weight) - gps_module_weight

# Print the type of each variable to demonstrate Python type system
print("Type of max_takeoff_weight:", type(max_takeoff_weight))
print("Type of frame_weight:", type(frame_weight))
print("Type of battery_weight:", type(battery_weight))
print("Type of num_propellers:", type(num_propellers))
print("Type of motor_weight:", type(motor_weight))
print("Type of is_gps_enabled:", type(is_gps_enabled))
print("Type of gps_module_weight:", type(gps_module_weight))

# Check whether the calculated payload is enough to carry a 1.8 kg camera
camera_weight = 1.8
can_carry_camera = max_payload >= camera_weight
print("Can carry 1.8 kg camera?", can_carry_camera)

# Convert max_takeoff_weight from kg to grams and store it as an integer
max_takeoff_weight_grams = int(max_takeoff_weight * 1000)
print("Max takeoff weight in grams:", max_takeoff_weight_grams)