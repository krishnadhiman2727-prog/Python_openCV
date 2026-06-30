# Take drone body weight as input from the user (in grams)
body_weight = float(input("Body weight (in g): "))

# Take payload weight as input from the user (in grams)
payload_weight = float(input("Payload weight (in g): "))

# Calculate the total weight (in g) by adding body weight and payload weight
total_weight = body_weight + payload_weight

# Converting total weight to kg
total_weight_kg = total_weight / 1000

# Display the total weight to the user
print(total_weight_kg, "kg")

# Check whether the total weight is greater than 2 kg
if total_weight_kg > 2:
    print("Total weight is greater than 2 kg")
else:
    print("Total weight is less than 2 kg")