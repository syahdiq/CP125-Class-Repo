def has_warming_trend(temps):
    for i in range(len(temps) - 2):
        if temps[i] < temps[i + 1] < temps[i + 2]:
            return True
    return False
