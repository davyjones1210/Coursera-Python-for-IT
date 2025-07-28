#!/usr/bin/env python3

import os
from PIL import Image

image_dir = '~/supplier-data/images'  # source images path

for filename in os.listdir(image_dir):
    if filename.endswith(".tiff") or filename.endswith(".tif"):
        try:
            filepath = os.path.join(image_dir, filename)
            img = Image.open(filepath)

            # Convert RGBA to RGB
            img = img.convert('RGB')

            # Resize the image
            resized_img = img.resize((600, 400))

            # Save the image in JPEG format
            new_filename = os.path.splitext(filename)[0] + '.jpeg'
            new_filepath = os.path.join(image_dir, new_filename)
            resized_img.save(new_filepath, "JPEG")

            print(f"Processed: {filename} -> {new_filename}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")

print("Image processing complete.")