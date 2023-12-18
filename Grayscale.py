import common
howard_pic = common.read_file("logo.jpeg")
def grayscale(image_matrix):
    for row in range(len(image_matrix)):
        for col in range(len(image_matrix[row])):
            r, g, b = image_matrix[row][col]

            gray_value = (r + g + b) // 3
            image_matrix[row][col] = [gray_value, gray_value, gray_value]

    return image_matrix


grayscale_howard_pic = grayscale(howard_pic)
common.write_file("grayscale_logo.jpeg", grayscale_howard_pic)
