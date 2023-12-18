import common
howard_pic = common.read_file("logo.jpeg")
def flip(image_matrix):
    flipped_image = image_matrix[::-1]
    return flipped_image


flipped_howard_pic = flip(howard_pic)
common.write_file("flipped_logo.jpeg", flipped_howard_pic)
