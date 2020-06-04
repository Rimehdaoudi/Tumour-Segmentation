# Import the required libraries.
from Converter import Convert
from Display import ImageDisplay
from Load import LoadData

# Main function.
if __name__ == "__main__":

    # Set the directory.
    myDirImages = '../Dataset/Pre-op/'
    myDirMasks = '../Dataset/Masks/'
    
    # Convert the dataset to nii.gz format.
    conv = Convert(myDir)
    conv.conversion()

    # Display the images.
    img = ImageDisplay(myDir)
    img.displayImage('01_preop_mri.nii', 6, 0, 30)

    # Resampled the images.
    dataLoad = LoadData(myDirImages, myDirMasks)
    image = dataLoad.loadImage("01_preop_mri.nii.gz")

    # Downsample
    downSampledImage = dataLoad.downsampledImage(image)

    # Upsample
    upSampledImage = dataLoad.upsampledImage(image)

    # Re-display the images.
    disp = ImageDisplay(myDirImages, myDirMasks)
    disp.displayResampledImage(downSampledImage, 6, 0, 10)
