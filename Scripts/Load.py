# Import the required libraries.
import os
import numpy as np
import nibabel as nib

# Create the Load Data class.
class LoadData(object):
    
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

    def retrieveData(self, images):
        imageData = []
        for i in range(len(images)):
            self.data = images[i].get_fdata()
            imageData.append(self.data)
        return imageData
