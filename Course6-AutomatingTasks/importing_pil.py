import PIL


#help(PIL)

from PIL import Image
im = Image.open(r"hopper.jpeg")
im.rotate(45).show()
# The code imports the PIL library, opens an image file named "bride.jpg", rotates it by 45 degrees, and displays the rotated image.
