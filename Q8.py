# Define sets for planned, restricted, and cleared zones
planned_zones = {"Z1", "Z2", "Z3", "Z5", "Z7"}
restricted_zones = {"Z3", "Z5", "Z6", "Z8"}
cleared_zones = {"Z1", "Z2", "Z3", "Z4", "Z5", "Z6", "Z7", "Z8"}

# Find which planned zones are restricted using set intersection
conflict_zones = planned_zones & restricted_zones
print("Planned zones that are restricted:", conflict_zones)

# Find zones that are planned but NOT restricted using set difference
safe_zones = planned_zones - restricted_zones
print("Safe zones (planned but not restricted):", safe_zones)

# Find zones in either planned or restricted, but NOT both (symmetric difference)
symmetric_diff = planned_zones ^ restricted_zones
print("Symmetric difference:", symmetric_diff)

# Check if planned_zones is a subset of cleared_zones
is_subset = planned_zones.issubset(cleared_zones)
print("Planned zones are a subset of cleared zones:", is_subset)

# Add "Z9" to planned_zones and remove "Z7" (added by mistake)
planned_zones.add("Z9")
planned_zones.discard("Z7")

# Print the count of unique zones across all three sets combined using union
all_zones = planned_zones | restricted_zones | cleared_zones
print("Count of unique zones across all sets:", len(all_zones))