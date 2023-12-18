import common
my_pic = common.read_file("6EC6C392-C041-4C18-88C6-FDD45679797A.jpeg")
def threshold(image_matrix, red_min, red_max, green_min, green_max, blue_min, blue_max):
    height = len(image_matrix)
    width = len(image_matrix[0])
    thresholded_image = [[(0, 0, 0) for _ in range(width)] for _ in range(height)]

    for y in range(height):
        for x in range(width):
            r, g, b = image_matrix[y][x]

            if red_min <= r <= red_max and green_min <= g <= green_max and blue_min <= b <= blue_max:
                thresholded_image[y][x] = (r, g, b)

    return thresholded_image

red_min = 0
red_max = 120
green_min = 0
green_max = 200
blue_min = 0
blue_max = 200


thresholded_my_pic = threshold(my_pic, red_min, red_max, green_min, green_max, blue_min, blue_max)
common.write_file("6EC6C392-C041-4C18-88C6-FDD45679797A.jpeg", thresholded_my_pic)
