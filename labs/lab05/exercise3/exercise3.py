
def find_bottleneck_index(traceroute):
    max_jump = 0
    max_index = 0
    for i in range(len(traceroute)):
        traceroute_prev, latency_prev = traceroute[i - 1]
        traceroute_curr, latency_curr = traceroute[i]

        jump = latency_curr - latency_prev

        if jump > max_jump:
            max_jump = jump
            max_index = i - 1

        highest = max_index
    return highest



# (hop_number, latency_in_ms)
traceroute = ((1, 5), (2, 8), (3, 45), (4, 48), (5, 50))
result = find_bottleneck_index(traceroute)
print(f"Bottleneck Index: {result}")  # Expected: 1
