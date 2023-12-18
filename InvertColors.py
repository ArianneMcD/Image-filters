import common
howard_pic = common.read_file("logo.jpeg")
def invert_colors(image_matrix):
    inverted_image = [[[(255 - pixel[i]) for i in range(3)] for pixel in row] for row in image_matrix]
    return inverted_image


inverted_howard_pic = invert_colors(howard_pic)
common.write_file("new_logo.jpeg", inverted_howard_pic)
