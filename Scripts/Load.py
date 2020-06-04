# Import the required libraries.
import os
import numpy as np
import nibabel as nib
from nilearn.image import smooth_img
from nilearn.image import resample_img

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
        self.files = os.listdir(self.dir)
        data_all = []
        for i in self.files:
            self.image = nib.load(self.dirImages + i)
            self.imageData = self.image.get_fdata()
            data_all.append(self.imageData)
        return data_all

    # Smooth an image.
    def smoothImage(self, image):
        smoothedImage = smooth_img(image)
        return smoothedImage

    # Smooth a list of images.
    def smoothImages(self, images):
        smoothedImages = smooth_image(images)
        return smoothedImages

    # Load a single tumour mask.
    def loadMask(self, dataFile):
        mask = nib.load(self.dirMask + dataFile)
        return mask

    # Load the tumour masks and store them as a list.
    def loadMasks(self):
        self.files = os.listdir(self.dir)
        data_all = []
        for i in self.files:
            self.image = nib.load(self.dirMask + i)
            self.imageData = self.image.get_fdata()
            data_all.append(self.imageData)
        return data_all

    # Downsample an MRI image.
    def downsampledImage(self, image):
        downsampledImage_ = resample_img(image, target_affine = np.eye(3)*2., interpolation = 'nearest')
        print("Original Image Shape: ", image.shape)
        print("New Image Shape: ", downsampledImage_.shape)
        return downsampledImage_

    # Upsampled an MRI image.
    def upsampledImage(self, image):
        upsampledImage = resample_img(image, target_affine = np.eye(3)*0.5, interpolation = 'nearest')
        print("Original Image Shape: ", image.shape)
        print("New Image Shape: ", upsampledImage.shape)
        return upsampledImage
        
