# Import the required libraries.
import os
import cv2
import numpy as np
import nibabel as nib
from sklearn.model_selection import train_test_split

# Create the Load Data class.
class LoadData3D(object):
    
    # Class Constructor.
    def __init__(self, directoryImages = " ", directoryMask = " "):
        self.dirImages = directoryImages
        self.dirMask = directoryMask

    # Load a single image.
    def loadImage(self, dataFile):
        image = nib.load(self.dirImages + dataFile)
        return image

    # Load the images and store in a list.
    def loadImages(self):
        self.files = os.listdir(self.dirImages)
        data_all = []
        for i in self.files:
            self.images = nib.load(self.dirImages + i)
            data_all.append(self.images)
        return data_all

    # Load a single tumour mask.
    def loadMask(self, dataFile):
        mask = nib.load(self.dirMask + dataFile)
        return mask

    # Load the tumour masks and store them as a list.
    def loadMasks(self):
        self.files = os.listdir(self.dir)
        data_all = []
        for i in self.files:
            self.images = nib.load(self.dirMask + i)
            data_all.append(self.images)
        return data_all

    def getData(self, image):
        data = image.get_fdata()
        return data

    def retrieveData(self, images):
        imageData = []
        for i in range(len(images)):
            self.data = images[i].get_fdata()
            imageData.append(self.data)
        return imageData

# Class for 2-Dimensional data
class LoadData2D(object):

    # Constructor
    def __init__(self, imageDir = " ", maskDir = " "):
        self.imgDir = imageDir
        self.mDir = maskDir

    # Load in the 2D images using opencv2
    def loadImages2D(self, sigma, IMG_SIZE):
       dataset = []
       self.files = os.listdir(imgDir)
       for i in self.files:
           try:   
               self.img = cv2.imread(imgDir, cv2.IMREAD_GRAYSCALE)
               self.blur = cv2.GaussianBlur(self.img, (sigma,sigma), 0)
               new_img = cv2.resize(self.blur, (IMG_SIZE, IMG_SIZE), interpolation = cv2.INTER_AREA)
               dataset.append(new_img)
           except Exception as e:
               pass
    return dataset

    # X = Images and y = Masks (Must be arrays not objects!)
    def splitData(self, images, masks, splitSize):
        X_train, X_test, y_train, y_test = train_test_split(images, masks, test_size = splitSize)
        return X_train, X_test, y_train, y_test



