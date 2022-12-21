from PIL import Image, ImageEnhance, ImageFilter
import os

# Set the input and output directories
input_dir = "/home/shridhar/Downloads/Images"
output_dir = "/home/shridhar/Downloads/editedImages"

# Iterate through all the files in the input directory
for file in os.listdir(input_dir):
    # Check if the file is an image
    if file.endswith('.jpg') or file.endswith('.png'):
        # Open the image file
        image = Image.open(os.path.join(input_dir, file))

        # Edit the image here(sharpen and monochrome filter)
        edit = image.filter(ImageFilter.SHARPEN).convert('L')

        # contrast
        factor = 1.5
        enhancer = ImageEnhance.Contrast(edit)
        edit = enhancer.enhance(factor)

        # Save the edited image to the output directory
        edit.save(os.path.join(output_dir, file))

print('Done editing the photos!!')
