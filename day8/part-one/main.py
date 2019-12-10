def build_image(filepath,width, height):
    image = []
    layer = []
    row = []
    with open(filepath) as f:
        for line in f:
            for num in list(line):
                if len(row) == width:
                    layer.append(row)
                    row = []
                if len(layer) == height:
                    image.append(layer)
                    layer = []
                row.append(int(num))
    if len(row) == width:
        layer.append(row)
        row = []
    if len(layer) == height:
        image.append(layer)
        layer = []
    return image

def digit_count(layer, digit):
    count = 0
    for row in layer:
        for number in row:
            if number == digit:
                count += 1
    return count




if __name__ == "__main__":
    image = build_image("../input.txt", 25, 6)

    min_zero_layer = min(image, key=lambda i: digit_count(i, 0))
    print(digit_count(min_zero_layer, 1) * digit_count(min_zero_layer, 2))