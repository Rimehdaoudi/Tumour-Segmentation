# Import the required libaries
import numpy as np
import skimage.io

class Evaluate(object):

    def __init__(self, pred_image, gt_image):
        self.pred_image = pred_image
        self.gt_image = gt_image

    def cm_terms(self):
        n11 = n12 = n21 = n22 =0
        [rows,cols] = self.gt_image.shape

        for i in range(rows):
            for j in range(cols):
                if self.gt_image[i,j]==0 and self.pred_image[i,j]==0:
                    n11 = n11+1
                if self.gt_image[i,j]==0 and self.pred_image[i,j]>=1:
                    n12 = n12 + 1
                if self.gt_image[i,j]>=1 and self.pred_image[i,j]==0:
                    n21 = n21 + 1
                if self.gt_image[i,j]>=1 and self.pred_image[i,j]>=1:
                    n22 = n22 + 1

        return n11, n12, n21, n22

    def pixel_accuracy(self):

        n11, n12, n21, n22 = Evaluate.cm_terms(self)
        t1 = n11 + n12
        t2 = n21 + n22

        if (t1+t2) == 0:
            pa = 0
        else:
            pa = float(n11+n22)/float(t1+t2)
        return pa

    def mean_accuracy(self):

        n11, n12, n21, n22 = Evaluate.cm_terms(self)
        t1 = n11 + n12
        t2 = n21 + n22

        if t1 == 0 and t2 != 0:
            ma = float(n22)/float(t2)
        if t1 != 0 and t2 == 0:
            ma = float(n11)/float(t1)
        if t1 == 0 and t2 == 0:
            ma = 0
        else:
            ma = (float(n11)/float(t1) + float(n22)/float(t2))/2
        return ma

    def IOU(self):
        intersection = np.logical_and(self.gt_image, self.pred_image)
        union = np.logical_or(self.gt_image, self.pred_image)
        iou_score = np.sum(intersection) / np.sum(union)
        return iou_score

    def mean_IOU(self):

        n11, n12, n21, n22 = Evaluate.cm_terms(self)
        t1 = n11 + n12
        t2 = n21 + n22

        if (t1+n21) == 0 and (t2+n12) != 0:
            mIOU = float(n22)/float(t2+n12)
        if (t1 + n21) != 0 and (t2 + n12) == 0:
            mIOU = float(n11)/float(t1+n21)
        else:
            mIOU = (float(n11)/float(t1+n21)  + float(n22)/float(t2+n12))/2
        return mIOU
    
    def fweight_IOU(self):

        n11, n12, n21, n22 = Evaluate.cm_terms(self)
        t1 = n11 + n12
        t2 = n21 + n22

        fwIOU = float(float(t1*n11)/float(n11+n12+n21)  + float(t2*n22)/float(n12+n21+n22))/float(n11+n12+n21+n22)

        return fwIOU

    def roc(self):

        self.pred_image
        self.gt_image

        TP = TN = FP = FN = 0
        [rows, cols] = self.gt_image.shape

        for i in range(rows):
            for j in range(cols):
                if self.gt_image[i, j] >= 1 and self.pred_image[i, j] >= 1:
                    TP = TP + 1
                if self.gt_image[i, j] == 0 and self.pred_image[i, j] == 0:
                    TN = TN + 1
                if self.gt_image[i, j] == 0 and self.pred_image[i, j] >= 1:
                    FP = FP + 1
                if self.gt_image[i, j] >= 1 and self.pred_image[i, j] == 0:
                    FN = FN + 1

        if (FP+TN)==0:
            fpr = 0
        else:
            fpr = float(FP)/float(FP+TN)


        if (TP+FN)==0:
            tpr = 0
        else:
            tpr = float(TP)/float(TP+FN)

        return TP, TN, FP, FN, fpr, tpr


def readImage(PATH):
    return skimage.io.imread(PATH)

if __name__ == "__main__":
    PATH_MASKS = 'Masks/2.png'
    PATH_PRED = 'Results/2.png'

    target = readImage(PATH_MASKS)
    pred = readImage(PATH_PRED)

    val = Evaluate(pred, target)
    TP, TN, FP, FN, fpr, tpr = val.roc()

    print(" ")
    print("Evaluation Metrics", "\t\t\tROC")
    print("----------------------", "\t\t----------------------")
    pixel_acc = val.pixel_accuracy()
    print("Pixel Accuracy: ", str(round(pixel_acc, 3)), "\t\tTrue Positive's: ", str(TP))

    mean_acc = val.mean_accuracy()
    print("Mean Accuracy: ", str(round(mean_acc, 3)), "\t\tFalse Positive's: ", str(FP))

    mean_IOU = val.mean_IOU()
    print("Mean IOU: ", str(round(mean_IOU, 3)), "\t\tTrue Negative's: ", str(TN))

    IOU = val.IOU()
    print("IOU: ", str(round(IOU, 3)), "\t\t\tFalse Negative's: ", str(FN))

    weight_IOU = val.fweight_IOU()
    print("Weighted IOU: ", str(round(weight_IOU, 3)), "\t\tTrue Positive Rate: ", str(round(tpr, 3)))
    print("----------------------", "\t\t----------------------")
