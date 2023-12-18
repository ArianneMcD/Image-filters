import common
howard_pic = common.read_file("logo.jpeg")
def red_stripe(image_matrix):
    stripe_height = 50
    stripe_num = 0

    for row in range(len(image_matrix)):
        if row % stripe_height == 0:
            stripe_num += 1
        for col in range(len(image_matrix[row])):
            if stripe_num % 2 == 0:
                image_matrix[row][col] = [255, image_matrix[row][col][1], image_matrix[row][col][2]]

    return image_matrix


red_filter = red_stripe(howard_pic)
common.write_file("new_logo.jpeg", red_filter)
print(howard_pic[0][0])

