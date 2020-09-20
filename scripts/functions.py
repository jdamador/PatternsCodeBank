
# Import libraries
import cv2
import imutils as imutils


class Transformations:
    #? Constructor
    def __init__(self, imagePath):
        self.imagePath = imagePath
        self.img = cv2.imread(imagePath)
        
    #? 1) Deploy a RGB for an specific pixel given by the user.
    def getPixelRGB(self, posX, posY):
        (B, G, R) = self.img[posX, posY]
        print("These are the values for [R, G, B] composition for the specific pixel checked: \nR = {}, G = {} and B = {}".format(R, G, B))

    #? 2) Extract a region of interest using coordinates given by the user.
    def getROI(self, init, end):
        roi = self.img[init[0]: init[1], end[0]:end[1]];
        self.showImg('ROI Request', roi)

    #? 3) Allow to adjust the size of an image requesting a new
    #  dimension in pixels and display the resulting image
    def getImageResize(self, image, pixels):
        resized = cv2.resize(image, (pixels, pixels))
        self.showImg('Fixed Resizing', resized)

    #? 4) Resize an image but without altering the appearance
    def getImageResizeWithoutAltheringAppearance(self, image):
        resized = imutils.resize(image, width=300)
        self.showImg("Imutils Resize", resized)

    #? 5) Rotate an image the number of degrees required
    def getImageRotation(self, image, degrees):
        rotated = imutils.rotate(image, degrees)
        self.showImg("Imutils Rotation", rotated)
        
        
    #? 6) Smoothing an image using Gaussian Blur
    def getGaussianBlurImage(self):
        blurred = cv2.GaussianBlur(self.img, (11, 11), 0)
        self.showImg('Smoothing Image', blurred)
        
    #? Simple method to show a image.
    def showImg(self, label, image):
        cv2.imshow(label, image)
        cv2.waitKey(0)