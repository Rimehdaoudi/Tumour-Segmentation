# Import the required libraries.
import cv2
import numpy as np
import matplotlib.pyplot as plt

class Threshold(object):

    # Class constructor, assign image and mask.
    def __init__(self, image):
        self.image = image

    # Strips the skull of the brain scan (Transversal).
    def skullStrip(self):
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.ret, self.thresh = cv2.threshold(self.gray_image, 0, 255, cv2.THRESH_OTSU)
        self.colormask = np.zeros(self.image.shape, dtype=np.uint8)
        self.colormask[self.thresh != 0] = np.array((0, 0, 255))
        self.blended = cv2.addWeighted(image, 0.7, self.colormask, 0.1,0) 

        self.ret, self.markers = cv2.connectedComponents(self.thresh)
        self.marker_area = [np.sum(self.markers == m) for m in range(np.max(self.markers)) if m != 0] 
        self.largest_component = np.argmax(self.marker_area) + 1              
        self.brain_mask = self.markers == self.largest_component

        brain_out = self.image.copy()
        brain_out[self.brain_mask==False] = (0,0,0)
        
        plt.subplot(121)
        plt.gca().set_title("Original"), plt.imshow(self.image, cmap = 'gray')
        plt.xticks([]), plt.yticks([])

        plt.subplot(122)
        plt.gca().set_title("Skull Stripped"), plt.imshow(brain_out, cmap = 'gray')
        plt.xticks([]), plt.yticks([])
        plt.show()

        return brain_out

    # Apply a median blur to a skull stripped image.
    def filter(self, stripped_image, kernel):
        median = cv2.medianBlur(stripped_image, kernel)

        plt.subplot(121)
        plt.gca().set_title("Original"), plt.imshow(self.image, cmap = 'gray')
        plt.xticks([]), plt.yticks([])

        plt.subplot(122)
        plt.gca().set_title("Median Blur"), plt.imshow(median, cmap = 'gray')
        plt.xticks([]), plt.yticks([])
        plt.show()

        return median

    # Apply otsu's thresholding.
    def otsuThreshold(self, stripped_image, filtered_image):
        self.retval, self.threshold = cv2.threshold(filtered_image, 190, 255, cv2.THRESH_BINARY)

        plt.subplot(121)
        plt.gca().set_title("Original"), plt.imshow(stripped_image, cmap = 'gray')
        plt.xticks([]), plt.yticks([])

        plt.subplot(122)
        plt.gca().set_title("Segmented"), plt.imshow(self.threshold, cmap = 'gray')
        plt.xticks([]), plt.yticks([])
        plt.show()


# Main method.
if __name__ == "__main__":
    
    image = cv2.imread('../../Dataset/UNET-Data/Transversal/Image_12_Transversal_108.png')

    thres = Threshold(image)
    skull_stripped = thres.skullStrip()
    median = thres.filter(skull_stripped, 5)
    thres.otsuThreshold(skull_stripped, median)