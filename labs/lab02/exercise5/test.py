def is_valid_triangle (side_1, side_2, side_3):
    if side_1 + side_2 > side_3:
        return True
    elif side_1 + side_3 > side_2:
        return True
    elif side_2 + side_3 > side_1:
        return True
    else:
        return False
    
    