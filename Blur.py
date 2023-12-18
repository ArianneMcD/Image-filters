import common
import copy
howard_pic = common.read_file("logo.jpeg")
def blur(image_matrix):
    blurred_image = copy.deepcopy(image_matrix)
    for row in range(1, len(image_matrix) - 1):
        for col in range(1, len(image_matrix[row]) - 1):
            neighbors = [
                blurred_image[row - 1][col - 1],
                blurred_image[row - 1][col],
                blurred_image[row - 1][col + 1],
                blurred_image[row][col - 1],
                blurred_image[row][col + 1],
                blurred_image[row][col],
                blurred_image[row + 1][col - 1],
                blurred_image[row + 1][col],
                blurred_image[row + 1][col + 1]
            ]

            red_total = 0
            for pixel in neighbors:
                red_total = red_total + pixel[0]
            red_value = red_total // 9

            green_total = 0
            for pixel in neighbors:
                green_total = green_total + pixel[1]
            green_value = green_total // 9

            blue_total = 0
            for pixel in neighbors:
                blue_total = blue_total + pixel[2]
            blue_value = blue_total // 9

            image_matrix[row][col] = [red_value, green_value, blue_value]

    return image_matrix

image = common.read_file("logo.jpeg")
blur_filter = blur(howard_pic)
common.write_file("blurred_logo.jpeg", blur_filter)

