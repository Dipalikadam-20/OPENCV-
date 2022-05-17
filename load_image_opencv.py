# USAGE
# python load_image_opencv.py --image 30th_birthday.png


# import the packages
import argparse
import cv2

print("OpenCV version: ")
print(cv2.__version__)


# To pass the image using command line argument, lets construct the argument parser and parse the argument
aug_parser = argparse.ArgumentParser()
aug_parser.add_argument("-i", "--image", required=True, help="path to input image")
aug_parser.add_argument("-o", "--outputimage", required=True, help="path to output image")
args= vars(aug_parser.parse_args())

#load the image from the disk using "cv2.imread()" function
image = cv2.imread(args["image"])
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# get the spatial dimensions including width,height and number of channels
(h, w, c) = image.shape[:3]
(h, w) = gray_image.shape[:2]


# Lets display the Color image width, height, and number of channels on the terminal
print("Spatial Dimensions of Colored Image")
print("width: {} pixels".format(w))
print("height: {} pixels".format(h))
print("channels: {}".format(c))

# Lets display the Gray image width, height, and number of channels on the terminal
print("Spatial Dimensions of Gray Image")
print("width: {} pixels".format(w))
print("height: {} pixels".format(h))
#print("channels: {}".format(c))

# lets show the image displaying the title
cv2.imshow("Loaded Color Image", image)
cv2.imshow("Loaded Gray Image", gray_image)
# wait for the keypress
cv2.waitKey(0)

# save the image back to the disk, opencv will convert the image into different filetype automatically
#cv2.imwrite("saved_image.jpg", image)
cv2.imwrite(args["outputimage"], image)

cv2.destroyAllWindows()
