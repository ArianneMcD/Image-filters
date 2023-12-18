import common
import random

howard_pic = common.read_file("logo.jpeg")
def broken_tv_filter(image_matrix):
    def apply_noise(pixel, noise_intensity):
        # Add random noise to each color channel
        noise = [random.randint(-noise_intensity, noise_intensity) for _ in range(3)]
        return [min(255, max(0, pixel[i] + noise[i])) for i in range(3)]

    def add_horizontal_lines(image_matrix, line_intensity, line_spacing):
        for row in range(0, len(image_matrix), line_spacing):
            for col in range(len(image_matrix[row])):
                for i in range(3):  # Apply to each color channel
                    image_matrix[row][col][i] = max(0, image_matrix[row][col][i] - line_intensity)
        return image_matrix

    def shift_color_channels(pixel, shift_intensity):
        # Randomly shift color channels to create color separation
        shift = random.randint(-shift_intensity, shift_intensity)
        return [(pixel[(i + shift) % 3]) for i in range(3)]

    # Apply noise to simulate screen interference
    noise_intensity = 120  # Adjust this value for the desired level of noise
    distorted_image = [[apply_noise(pixel, noise_intensity) for pixel in row] for row in image_matrix]

    # Add horizontal lines to create a broken effect
    line_intensity = 90  # Adjust this value for the thickness of lines
    line_spacing = 127  # Adjust this value for the frequency of lines
    distorted_image = add_horizontal_lines(distorted_image, line_intensity, line_spacing)

    # Shift color channels to create color separation
    shift_intensity = 150  # Adjust this value for the intensity of the color separation
    distorted_image = [[shift_color_channels(pixel, shift_intensity) for pixel in row] for row in distorted_image]

    return distorted_image


broken_tv_howard_pic = broken_tv_filter(howard_pic)
common.write_file("broken_tv_logo.jpeg", broken_tv_howard_pic)
