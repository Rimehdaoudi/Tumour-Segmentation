# Import the required libraries.
from Converter import Convert
from Display import ImageDisplay

# Main function.
if __name__ == "__main__":

    # Set the directory.
    myDir = '../Dataset/Pre-op/'
    
    # Convert the dataset.
    conv = Convert(myDir)
    conv.conversion()

    # Display the images.
    img = ImageDisplay(myDir)
    img.displayImage('01_preop_mri.nii', 6, 0, 30)
