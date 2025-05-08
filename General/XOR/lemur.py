from PIL import Image, ImageChops
im1 = Image.open('lemur.png')
im2 = Image.open('flag.png')

im3 = ImageChops.add(ImageChops.subtract(im2, im1), ImageChops.subtract(im1, im2))
im3.show()

##performs pixel-wise subtraction to calculate 
# the difference between the two images using ImageChops.subtract(). 
# Then, it adds the two subtracted images together to highlight differences, creating a new image im3.
# Finally, im3.show() displays the resulting image. 