#  if we wanted to resize an image and save the new image with a new name, we could do it with:

from PIL import Image
im = Image.open("example.jpg")
new_im = im.resize((640,480))
new_im.save("example_resized.jpg")


# Or, if we want to rotate an image, we can use code like this:
from PIL import Image
im = Image.open("example.jpg")
new_im = im.rotate(90)
new_im.save("example_rotated.jpg")

# we can even combine these operations into just one line that rotates, resizes, and saves:
from PIL import Image
im = Image.open("example.jpg")
im.rotate(180).resize((640,480)).save("flipped_and_resized.jpg")


