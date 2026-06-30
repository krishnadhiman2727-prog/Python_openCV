# Define the fleet dictionary
fleet = {
    "PX4_001": {"battery": 87, "altitude": 120, "status": "active", "payload_kg": 1.2},
    "PX4_002": {"battery": 23, "altitude": 0, "status": "grounded", "payload_kg": 0},
    "PX4_003": {"battery": 56, "altitude": 85, "status": "active", "payload_kg": 0.8},
    "PX4_004": {"battery": 11, "altitude": 30, "status": "returning", "payload_kg": 0.5},
}

# Add a new drone "PX4_005" to the fleet dictionary
fleet["PX4_005"] = {"battery": 95, "altitude": 0, "status": "standby", "payload_kg": 0}

# Remove "PX4_002" using .pop() and print its details before removal
removed_drone = fleet.pop("PX4_002")
print("Removed drone details:", removed_drone)

# Print all active drones and their battery levels
print("Active drones:")
for drone_id, stats in fleet.items():
    if stats["status"] == "active":
        print(f"  {drone_id}: Battery {stats['battery']}%")

# Find the drone with the lowest battery among drones currently in the air (altitude > 0)
drones_in_air = {k: v for k, v in fleet.items() if v["altitude"] > 0}
lowest_battery_drone = min(drones_in_air, key=lambda x: drones_in_air[x]["battery"])
print("Drone with lowest battery in air:", lowest_battery_drone)

# Update every drone with battery < 30 to status "critical_low_battery"
for drone_id, stats in fleet.items():
    if stats["battery"] < 30:
        stats["status"] = "critical_low_battery"

# Print a final formatted fleet summary
print("\nFinal Fleet Summary:")
print("-" * 40)
for drone_id, stats in fleet.items():
    print(f"{drone_id} | Batt: {stats['battery']}% | Alt: {stats['altitude']}m | Status: {stats['status']} | Payload: {stats['payload_kg']}kg")