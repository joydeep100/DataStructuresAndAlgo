def compute_closest_to_zero(ts):

    if not ts: return 0
    closest = float('inf')
    closest_idx = -1
    
    for i, t in enumerate(ts):
        if abs(t) < closest:
            closest = abs(t)
            closest_idx = i

    return ts[closest_idx]

print(compute_closest_to_zero([-10, -10]))