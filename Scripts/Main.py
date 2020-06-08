# Import the required libraries.
from Converter import Convert
from Display import ImageDisplay
from Load import LoadData
from Preprocess import Process

from nilearn.image.image import mean_img
from nilearn.plotting import plot_epi, show, plot_roi
from nilearn.masking import compute_epi_mask

# Main function.
if __name__ == "__main__":

    # Set the directory.
    myDirImages = '../Dataset/Pre-op/'
    myDirMasks = '../Dataset/Masks/'

    # Display the images.
    img = ImageDisplay(myDirImages, myDirMasks)
    img.displayImages('01_preop_mri.mnc', 6, 0, 30)

    # Resampled the images.
    dataLoad = LoadData(myDirImages, myDirMasks)
    images = dataLoad.loadImages()

    # Smooth the images (using the image object rather than the data.)
    pre = Process()
    smoothenedImages = pre.smoothImages(images, 0.3)

    # Load the image data.
    imageData = dataLoad.retrieveData(smoothenedImages)
    maskData = dataLoad.retrieveData(smoothenedMasks)
    
    # Resample the images.
    resampledImages = pre.resampleImages(imageData, 256)
    resampledMasks = pre.resampleImages(maskData, 256) 

    # Re-display the resampled images.
    img.displayResampledImage(resultData, 3, 10, 5)
    img.displayResampledImage(resampledMasks, 4, 3, 3)

