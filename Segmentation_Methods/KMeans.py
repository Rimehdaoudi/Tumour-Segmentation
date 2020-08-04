# Import the required libraries.
import os
import cv2
import warnings
import numpy as np
# import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from time import time

warnings.filterwarnings("ignore")


# K-Means Image Segmentation.
class KMeansSegment(object):
    # Read in the images.
    def readImage(self):
        folder = '../Evaluation Scans/Transversal/'
        list_images = os.listdir(folder)
        list_img = []
        for i in list_images:
            path = folder+i
            img = cv2.imread(path)
            img = cv2.resize(img, (128, 128))
            rgb_img = img.reshape((img.shape[0] * img.shape[1], 3))
            list_img.append(rgb_img)

        return list_img

    # Compute the area of the objects in a binary image.
    def bwarea(self, img):
        row = img.shape[0]
        col = img.shape[1]
        total = 0.0
        for r in range(row-1):
            for c in range(col-1):
                sub_total = img[r:r+2, c:c+2].mean()
                if sub_total == 255:
                    total += 1
                elif sub_total == (255.0/3.0):
                    total += (7.0/8.0)
                elif sub_total == (255.0/4.0):
                    total += 0.25
                elif sub_total == 0:
                    total += 0
                else:
                    r1c1 = img[r, c]
                    r1c2 = img[r, c+1]
                    r2c1 = img[r+1, c]
                    r2c2 = img[r+1, c+1]

                    if (((r1c1 == r2c2) & (r1c2 == r2c1)) & (r1c1 != r2c1)):
                        total += 0.75
                    else:
                        total += 0.5
        return total

    # Change the cluster color.
    def change_color_kmeans(self, predict_img, clusters):
        img = []
        for val in predict_img:
            img.append(clusters[val])
        return img

    # Implementing K-Means algorithm.
    def process(self, list_img, clusters):
        self.seg_array = []
        for rgb_img in list_img[:]:
            img = np.reshape(rgb_img, (128, 128, 3)).astype(np.uint8)
            shape = np.shape(img)

            clt = KMeans(n_clusters=clusters, n_jobs=4)
            clt.fit(rgb_img)
            predict_img = clt.predict(rgb_img)
            new_img = self.change_color_kmeans(
                    predict_img,
                    clt.cluster_centers_
                    )
            kmeans_img = np.reshape(new_img, shape).astype(np.uint8)
            new_time = time()

            self.ret, self.seg_img = cv2.threshold(
                    kmeans_img,
                    np.max(kmeans_img) - 1,
                    255,
                    cv2.THRESH_BINARY
            )
            print("Time:", time() - new_time, 'seconds')
            print("BWAREA:", self.bwarea(self.seg_img[:, :, 1]))

            self.seg_array.append(self.seg_img)

            """
            plt.subplot(131)
            plt.gca().set_title("Original"), plt.imshow(img)
            plt.xticks([]), plt.yticks([])

            plt.subplot(132)
            plt.gca().set_title("K-Means"), plt.imshow(kmeans_img)
            plt.xticks([]), plt.yticks([])

            plt.subplot(133)
            plt.gca().set_title("Segmented"), plt.imshow(self.seg_img)
            plt.xticks([]), plt.yticks([])
            plt.show()
            """

    def writeFile(self, OUTDIR):
        for i in range(len(self.seg_array)):
            cv2.imwrite(
                    OUTDIR +
                    "Result_" +
                    str(i) +
                    ".png",
                    self.seg_array[i]
            )


if __name__ == "__main__":
    OUTDIR = './KMeans Results/Transversal/'

    means = KMeansSegment()
    list_img = means.readImage()
    means.process(list_img, 4)
    means.writeFile(OUTDIR)
