# Import the required libraries.
import numpy as np
import nibabel as nib

# Create the Load Data class.
class LoadData(object):
    
    # Class Constructor.
    def __init__(self, directory = " "):
        self.dir = directory

    # Create the function to load a single image.
    def loadImage(self, dataFile):
        image = nib.load(self.dir + dataFile)
        return image
