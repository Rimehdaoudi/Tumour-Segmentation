# Import the required libraries.
import cv2
import numpy as np
from skimage.transform import resize
from nilearn.image import smooth_img, resample_to_img

# Pre-process class.
class Process(object):

    # Expand the dimensions of the image.
    def expandDims(self, image):
        expDim = np.expand_dims(image, axis=-1)
        print("Original Image Shape: ", image.shape)
        print("New Image Shape: ", expDim.shape)
        return expDim

    # Resample an image.
    def resampleImage(self, image, target):
        resampledImage = resize(image, (image.shape[0], target, target), mode = 'constant', anti_aliasing = True)
        print("Original Image Shape: ", image.shape)
        print("New Image Shape: ", resampledImage.shape)
        return resampledImage

    # Function to either upsample or downsample a list of images
    def resampleImages(self, images, target):
        sampledImages = []
        for i in range(len(images)):
            print("Original Shape: ", images[i].shape)
            sample = resize(images[i], (images[i].shape[0], target, target), mode = 'constant', anti_aliasing = True)
            sampledImages.append(sample)
            print("New Image Shape: ", sampledImages[i].shape)
            print("\n")
        return sampledImages

   # Smooth a list of images.
    def smoothImage(self, image, threshold):
        smoothedImage = smooth_img(image, threshold)
        return smoothedImage

    # Smooth a list of images.
    def smoothImages(self, images, threshold):
        smoothedImages = []
        for i in range(len(images)):
            smoothedImage = smooth_img(images[i], threshold)
            smoothedImages.append(smoothedImage)
            print("Image Smoothened")
        return smoothedImages

    # Resample the mask to the size of the MRI image.
    def resampleToImage(self, image, mask):
        resampledImage = resample_to_img(mask, image)
        return resampledImage

    # Resample the masks to the MRI images.
    def resampleToImages(self, images, masks):
        resampledImages = []
        for i in range(len(images)):
            resampledImage = resample_to_img(masks, images)
            resampledImages.append(resampledImage)
            print("Mask Resampled")
        return resampledImages

    # Extract each slice from an MRI image
    def sliceExtractor(self, imageData, numSlices, OUTDIR = ' ', coronal = False, sagittal = False, transversal = False):
        for i in range(numSlices):
            # Coronal
            if coronal == True:
                slices = imageData[:, i, :]
                flipVertical = cv2.flip(slices, 0)
                cv2.imwrite(OUTDIR + "Coronal_" + str(i) + ".png", flipVertical)
            # Sagittal
            elif sagittal == True:
                slices = imageData[:, :, i]
                flipVertical = cv2.flip(slices, 0)
                cv2.imwrite(OUTDIR + "Sagittal_" + str(i) + ".png", flipVertical)
            # Transversal
            elif transversal == True:
                slices = imageData[i, :, :]
                flipVertical = cv2.flip(slices, 0)
                cv2.imwrite(OUTDIR + "Transversal_" + str(i) + ".png", flipVertical)
            else:
                print("Failed")
                break
        print("Passed")


        

