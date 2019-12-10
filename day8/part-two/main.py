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
                row.append(num)
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
            if number == str(digit):
                count += 1
    return count

def decode_image(image):
    output = image[-1]
    i = len(image) - 2

    while i >= 0:
        for j in range(len(image[i])):
            for k in range(len(image[i][j])):
                if image[i][j][k] != "2":
                        output[j][k] = image[i][j][k]
        i -= 1
    return output


if __name__ == "__main__":
    image = build_image("../input.txt", 25, 6)
    with open("output.txt", "w") as f:
        for row in decode_image(image):
            f.write("".join(row) + "\n")
