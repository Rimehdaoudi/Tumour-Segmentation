# Import the required libraries.
from Converter import Convert
from Display import ImageDisplay
from Load import LoadData
from Preprocess import Process

# Main function.
if __name__ == "__main__":

    # Set the directory.
    myDirImages = '../Dataset/Pre-op/'
    myDirMasks = '../Dataset/Masks/'
    
    # Convert the dataset to nii.gz format.
    conv = Convert(myDir)
    conv.conversion()

    # Display the images.
    img = ImageDisplay(myDirImages, myDirMasks)
    img.displayImages('01_preop_mri.nii', 6, 0, 30)

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
    img.displayResampledImage(resampledImages, 4, 10, 30)
    img.displayResampledImage(resampledMasks, 4, 3, 3)

