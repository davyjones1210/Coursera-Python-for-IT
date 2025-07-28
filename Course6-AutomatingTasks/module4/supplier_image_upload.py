#!/usr/bin/env python3

import requests
import os

image_dir = 'supplier-data/images'  # Directory containing the JPEG images
upload_url = "http://localhost/upload/"  # URL to upload the images

for filename in os.listdir(image_dir):
    if filename.endswith(".jpeg"):
        image_path = os.path.join(image_dir, filename)
        try:
            with open(image_path, 'rb') as image_file:
                files = {'file': image_file}
                response = requests.post(upload_url, files=files)
                response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
                print(f"Image '{filename}' uploaded successfully. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error uploading image '{filename}': {e}")