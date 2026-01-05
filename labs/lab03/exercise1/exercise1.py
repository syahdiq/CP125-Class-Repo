def count_bright_spots(pixels):
    count = 0
    for i in range(1, len(pixels) - 1):
        if pixels[i] > pixels[i - 1] and pixels[i] > pixels[i + 1]:
            count += 1
    return count



