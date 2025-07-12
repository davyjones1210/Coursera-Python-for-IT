import os
import requests

feedback_dir = '/data/feedback'
website_url = 'http://35.231.135.54/feedback/'

for filename in os.listdir(feedback_dir):
    if filename.endswith(".txt"):
        filepath = os.path.join(feedback_dir, filename)
        with open(filepath, 'r') as f:
            lines = f.read().splitlines()
            feedback = {
                "title": lines[0],
                "name": lines[1],
                "date": lines[2],
                "feedback": lines[3],
            }

        try:
            response = requests.post(website_url, data=feedback)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            print(f"Feedback '{filename}' uploaded successfully. Status code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"Error uploading feedback '{filename}': {e}")