# Finding the resolution of a image

from PIL import Image

picture = Image.open("C:/Users/abhin/OneDrive/Desktop/IMG_20220122_132953.jpg")
#the directory of image should be copied from properties and back slashes '\' change to forward slashes'/'

width , height = picture.size

print(f"{width} x {height}")