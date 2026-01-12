import os
from PIL import Image

def print_image_sizes(image_folder):
    """
    Print the sizes (width and height) of all images in a folder.

    Args:
    image_folder (str): Path to the folder containing image files.
    """
    for image_file in os.listdir(image_folder):
        if image_file.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff')):
            image_path = os.path.join(image_folder, image_file)
            try:
                with Image.open(image_path) as img:
                    width, height = img.size
                    print(f"Image: {image_file}, Width: {width}, Height: {height}")
            except Exception as e:
                print(f"Error processing {image_file}: {e}")

# Example usage
image_folder = '/home/zzh/yolov10/data/night_sunny/images'  # Replace with the path to your image folder
print_image_sizes(image_folder)