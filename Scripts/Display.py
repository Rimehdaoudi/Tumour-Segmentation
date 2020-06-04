# Import the required libraries.
import matplotlib.pyplot as plt
from Load import LoadData

# Create the Image Display class.
class ImageDisplay(object):
    
    # Class Constructor.
    def __init__(self, directory = " "):
        self.dir = directory

    # Create the function to display a single image.
    def displayImage(self, dataFile, numImages, startSlice, incSlices):
        fig, ax = plt.subplots(1, numImages, figsize=[18, 6])
        self.image = LoadData(self.dir)
        self.img = self.image.loadImage(dataFile)
        self.imageData = self.img.get_fdata()

        # Loop through the parameter range.
        for i in range(numImages):
            ax[i].imshow(self.imageData[startSlice, :, :], 'gray')
            ax[i].set_xticks([])
            ax[i].set_yticks([])
            ax[i].set_title('Slice number: {}'.format(startSlice), color='r')
            startSlice += incSlices

        # Show the images.
        fig.subplots_adjust(wspace=0, hspace=0)
        plt.show()
