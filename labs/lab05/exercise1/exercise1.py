
def was_backward_detected(waypoints):
    for i in range(len(waypoints) - 1):
        previous_point = waypoints[i]
        current_point = waypoints[i + 1]

        prev_x = previous_point[0]
        prev_y = previous_point[1]

        curr_x = current_point[0]
        curr_y = current_point[1]

        if prev_x > curr_x or prev_y > curr_y:
            return True
        
    return False

    

# Test
waypoints = ((0, 0, 10), (5, 5, 12), (4, 6, 10), (10, 10, 15))
result = was_backward_detected(waypoints)
print(f"Backward Movement: {result}")  # Expected: True
