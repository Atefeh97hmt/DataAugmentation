
from PIL import Image, ImageOps
import os
import random

def augment_image(image_path, output_folder):
    try:
        # Open the image
        image = Image.open(image_path)

        # Define augmentation transformations
        def rotate_image(img):
            return img.rotate(random.choice([90, 180, 270]), resample=Image.Resampling.LANCZOS)

        def flip_image(img):
            return ImageOps.mirror(img) if random.choice([True, False]) else ImageOps.flip(img)

        def scale_image(img):
            scale_factor = random.uniform(0.8, 1.2)
            new_size = (int(img.width * scale_factor), int(img.height * scale_factor))
            return img.resize(new_size, resample=Image.Resampling.LANCZOS)

        # Apply augmentations
        augmented_images = [
            rotate_image(image),
            flip_image(image),
            scale_image(image)
        ]

        # Save augmented images
        base_name = os.path.basename(image_path)
        name, ext = os.path.splitext(base_name)
        if ext.lower() == '.png':
            for i, img in enumerate(augmented_images):
                augmented_path = os.path.join(output_folder, f"{name}_aug_{i}.png")
                img.save(augmented_path)
                print(f"Saved augmented image to {augmented_path}")

    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def augment_dataset(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith('.png'):
            image_path = os.path.join(input_folder, file_name)
            augment_image(image_path, output_folder)

# Example usage
input_folder = './signature'
output_folder = './augmented-images'
augment_dataset(input_folder, output_folder)
