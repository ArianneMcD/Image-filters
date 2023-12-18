import common
howard_pic = common.read_file("logo.jpeg")
def sepia(image_matrix):
    def apply_sepia(pixel):
        input_red, input_green, input_blue = pixel
        new_red = min(255, (input_red * 0.393 + input_green * 0.769 + input_blue * 0.189))
        new_green = min(255, (input_red * 0.349 + input_green * 0.686 + input_blue * 0.168))
        new_blue = min(255, (input_red * 0.272 + input_green * 0.534 + input_blue * 0.131))
        return [new_red, new_green, new_blue]

    sepia_image = [[apply_sepia(pixel) for pixel in row] for row in image_matrix]

    return sepia_image

sepia_howard_pic = sepia(howard_pic)
common.write_file("new_logo.jpeg", sepia_howard_pic)
