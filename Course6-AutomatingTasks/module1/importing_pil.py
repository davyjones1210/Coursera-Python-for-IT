import PIL
import io

#help(PIL)

from PIL import Image
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        img = Image.open(r"hopper.jpeg")
        rotated_img = img.rotate(45)
        img_io = io.BytesIO()
        rotated_img.save(img_io, 'JPEG')  # Specify JPEG format
        img_io.seek(0)
        return send_file(img_io, mimetype='image/jpeg')
    except Exception as e:
        return str(e)  # Return the error message

if __name__ == '__main__':
    app.run(debug=True)

# im = Image.open(r"hopper.jpeg")
# im.rotate(45).show()
# # The code imports the PIL library, opens an image file named "bride.jpg", rotates it by 45 degrees, and displays the rotated image.
