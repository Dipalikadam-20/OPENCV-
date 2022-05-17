# USAGE
# python accessing_pixel.py --image image1.png


# import the necessary packages

import argparse
import cv2


# construct the argument parser and parse the arguments
aug_parser = argparse.ArgumentParser()
aug_parser.add_argument("-i", "--image", help="path to input image")
args = vars(aug_parser.parse_args())



# load the image, grab its spatial dimensions (width and height),
# and then display the original image to our screen
image = cv2.imread(args["image"])
(h,w) = image.shape[:2]
cv2.imshow("Original image", image)


# images are simply NumPy arrays -- with the origin (0, 0) located at
# the top-left of the image
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))


# access the pixel located at x=50, y=20
#image[y,x] order to remember for image representation
(b, g, r) = image[20, 50]
print("Pixel at (50,20) - Red : {}, Green: {}, Blue: {}".format(r, g, b))

# update the pixel at (80, 30) and set it to red
image[30, 80] = (0, 0, 255)
(b, g, r) = image[30, 80]
print("Pixel at (80, 30) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# compute the center of the image, which is simply the width and height
# divided by two
(cX, cY) = (w // 2, h // 2)

# since we are using NumPy arrays, we can apply array slicing to grab
# large chunks/regions of interest from the image -- here we grab the
# top-left corner of the image
top_left = image[0:cY, 0:cX]
cv2.imshow("Top-Left Corner", top_left)

# in a similar fashion, we can crop the top-right, bottom-right, and
# bottom-left corners of the image and then display them to our
# screen
top_right = image[0:cY, cX:w]
bottom_right = image[cY:h, cX:w]
bottom_left = image[cY:h, 0:cX]
cv2.imshow("Top-Right Corner", top_right)
cv2.imshow("Bottom-Right Corner", bottom_right)
cv2.imshow("Bottom-Left Corner", bottom_left)

# set the top-left corner of the original image to be red (B, G, R)
image[0:cY, 0:cX] = (0, 0, 255)

# Show our updated image
cv2.imshow("Modified Image", image)
cv2.waitKey(0)