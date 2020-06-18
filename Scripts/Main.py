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

    # Load single image.
    image = nib.load(myDirImages + "02_preop_mri.mnc")
    masks = nib.load(myDirMasks + "02_two_tumor.mnc")

    # Retrieve the data 
    imageData = image.get_fdata()
    maskData = mask.get_fdata()

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
    imagesData = dataLoad.retrieveData(smoothenedImages)
    masksData = dataLoad.retrieveData(smoothenedMasks)
    
    # Resample the images.
    resampledImages = pre.resampleImages(imagesData, 256)
    resampledMasks = pre.resampleImages(masksData, 256) 

    # Re-display the resampled images.
    img.displayResampledImage(reData, 6, 50, 10)
    img.displayResampledImage(resampledMasks, 4, 3, 3)

    # Output directory
    OUTDIR = './Images/Patient 1/Coronal/'

    # Call the slice extractor (180 IS MAX!)
    pre.sliceExtractor(imageData, 180, OUTDIR, True, False, False)

    
