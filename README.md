# Brain tumour segmentation of Magnetic Resonance Images
This repository contains the python implementation used to segment tumours from 2D brain scans using the U-Net archietecture. The code was developed based on the research I carried out during my disertation for my MSc degree at University College Dublin where I explored medical image segmentation using a basic U-Net architecture and bechmarked its performance to other similar segmentation methods.

## Requirements
Please note that U-Net and LinkNet were implemented using **Tensorflow 2.0** and all scripts available are written in **python 3.8**. Using older versions of either software may cause conflicts and may hinder your ability to run each individual scripts. To install these requirements please see the following commands below.

```
pip install tensorflow
sudo apt-get install python3
```

Besides the listed requirements several scripts will also require you to install several packages that you may be missing from your most current installation of **python 3.8**. A list of the most un-common packages that were used during this project have been created so you can easily install these using the following commands.

```
pip install opencv-python
pip install nibabel
pip install nilearn
pip install scikit-fuzzy
```

## Dataset
The original 3-dimensional dataset used during the early stages of this project is **not** included with this repository, it can, however, be retrieved from [the following link](http://nist.mni.mcgill.ca/?page_id=672). Each 3-dimensional MRI brain scan was converted to a basic PNG image via the use of the **_slice extractor_** which can be found in **Preprocessing.py**. See later sections of this read me for a detailed tutorial on this procedure. The dataset extracted using this function can be retrived using [the following link](https://drive.google.com/drive/folders/1vG4Md-Orx3mkFFxunLLENBDPWciCIay-?usp=sharing). The dataset is structured so that it is easier to run your computations on one of three perspective planes. 

## Visualising & Preprocessing the data
Once you have downloaded the MRI data you can avail of the function created in **Load.py** to either load in a single 3-dimensional image or load in all MRI files which is stored in a basic list. The functions call the **_directory_** parameter to load the images from the selecting folder. These functions can also be used on any form of 3-dimensional imagery including DICOM and Nii files.

```python
def loadImages(self):
    self.files = os.listdir(self.dirImages)
    data_all = []
    for i in self.files:
        self.images = nib.load(self.dirImages + i)
        data_all.append(self.images)
    return data_all
```

The script **Preprocessing.py** contains many functions that you may use to preporcess your images. These functions are mainly suited to 2-dimensional images, however, the slice extractor is can only accecpt **_3-dimensional imagery_**. The **_slice extractor_** is a very simple function which loops through a list of MRI images and depending on the paramters provided by the user in their **_main_** the function will either extract a mask or a image on one of the three perspective planes. The function takes several self explanatory parameters, however, see the code below for an example on the extraction. 

```python
def sliceExtractor(self, imageData, numSlices, OUTDIR=' ', Image=False, Mask=False, coronal=False, sagittal=False, transversal=False):
    for i in range(numSlices):
        if Image:
            if coronal:
                slices = imageData[:, i, :]
                flipVertical = cv2.flip(slices, 0)
                cv2.imwrite(OUTDIR + "Coronal_" + str(i) + ".png", flipVertical)        
        .
        .
        .
```
