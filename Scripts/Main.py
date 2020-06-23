# Import the required libraries.
from Converter import Convert
from Display import ImageDisplay
from Load import LoadData3D, LoadData2D
from Preprocess import Process

# Main function.
if __name__ == "__main__":

    # Set the directory.
    myDirImages = '../Dataset/Original/Pre-op/'
    myDirMasks = '../Dataset/Original/Masks/'

    # Load single image.
    dataLoad = LoadData(myDirImages, myDirMasks)
    image = dataLoad.loadImage("04_preop_mri.mnc")
    mask = dataLoad.loadMask("04_tumor.mnc")
    print(image.shape)

    # Retrieve the data 
    imageData = dataLoad.getData(image)
    maskData = dataLoad.getData(mask)
    
    # Resample masks to target image.
    pre = Process()
    resampledImage = pre.resampleToImage(mask, image)
    resampledData = dataLoad.getData(resampledImage)

    # Output directory
    OUTDIR = '../Dataset/2D/Masks/Patient 4/Transversal/'

    # Call the slice extractor (180 IS MAX!)
    pre.sliceExtractor(resampledData, 180, OUTDIR, False, True, False, False, True) 
