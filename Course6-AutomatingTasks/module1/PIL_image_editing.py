import os
from PIL import Image

source_dir = '/home/student/images'
target_dir = '/opt/icons/'

# Process each image in the source directory
for filename in os.listdir(source_dir):
    try:
        filepath = os.path.join(source_dir, filename)
        img = Image.open(filepath)

        # Rotate 90 degrees clockwise
        rotated_img = img.rotate(-90)  # Negative angle for clockwise

        # Resize the image
        resized_img = rotated_img.resize((128, 128))

        # Save the image to the target directory in JPEG format
        new_filename = os.path.splitext(filename)[0] + '.jpeg'
        new_filepath = os.path.join(target_dir, new_filename)
        resized_img.convert('RGB').save(new_filepath, 'JPEG')  # Convert$

        print(f"Processed: {filename} -> {new_filename}")

    except Exception as e:
        print(f"Error processing {filename}: {e}")

print("Image processing complete.")