# Define the list of waypoints as coordinate tuples
waypoints = [(0, 0), (3, 4), (6, 8), (10, 8), (10, 0)]

def total_distance(waypoints, index=0):
    """Recursively compute the total path distance across all waypoints."""
    if index >= len(waypoints) - 1:
        return 0.0
    
    x1, y1 = waypoints[index]
    x2, y2 = waypoints[index + 1]
    
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return distance + total_distance(waypoints, index + 1)

def find_longest_leg(waypoints, index=0, max_dist=0.0):
    """Recursively find the longest single leg in the journey."""
    if index >= len(waypoints) - 1:
        return max_dist
    
    x1, y1 = waypoints[index]
    x2, y2 = waypoints[index + 1]
    
    current_distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    if current_distance > max_dist:
        max_dist = current_distance
        
    return find_longest_leg(waypoints, index + 1, max_dist)

# Display the results
print("Total path distance:", total_distance(waypoints))
print("Longest single leg:", find_longest_leg(waypoints))