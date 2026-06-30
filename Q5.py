# Define the list of altitudes recorded each second during the flight
altitudes = [0, 15, 42, 78, 120, 118, 115, 50, 20, 0]

# Find the maximum altitude and the second (index) it occurred
max_altitude = max(altitudes)
max_altitude_second = altitudes.index(max_altitude)
print("Maximum altitude:", max_altitude, "m at second", max_altitude_second)

# Calculate the average altitude and round to 2 decimal places
average_altitude = round(sum(altitudes) / len(altitudes), 2)
print("Average altitude:", average_altitude, "m")

# Create climb_rates list by calculating difference between consecutive altitudes
climb_rates = []
for i in range(len(altitudes) - 1):
    climb_rates.append(altitudes[i+1] - altitudes[i])
print("Climb rates:", climb_rates)

# Find the steepest climb (maximum positive value) and steepest descent (minimum value)
highest_climb = max(climb_rates)
steepest_descent = min(climb_rates)
print("Steepest climb:", highest_climb)
print("Steepest descent:", steepest_descent)

# Remove all zero-altitude entries and print the trimmed path
trimmed_path = [a for a in altitudes if a != 0]  # list comprehension
print("Trimmed path (no zeros):", trimmed_path)