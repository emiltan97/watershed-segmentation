import cv2 as cv 
import numpy as np

from matplotlib import pyplot as plt
from skimage.morphology import reconstruction

def imreconstruct (marker, mask, kernel) : 
    while True : 
        expanded = cv.dilate(marker, kernel, 1)
        cv.bitwise_and(expanded, mask, expanded)

        if (marker == expanded).all() : 
            return expanded

        marker = expanded

def imcomplement(image):
  """Equivalent to matlabs imcomplement function"""
  min_type_val = np.iinfo(image.dtype).min
  max_type_val = np.iinfo(image.dtype).max
  return min_type_val + max_type_val - image


if __name__ == "__main__" : 
    # Step 1 : Read in the color image and convert it to grayscale 
    img  = cv.imread('sample.png')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Step 2 : Use the gradient magnitude as the segmentation function 
    grad_x = cv.Sobel(gray, cv.CV_16S, 1, 0, ksize=3, scale=1, delta=0, borderType=cv.BORDER_DEFAULT)
    grad_y = cv.Sobel(gray, cv.CV_16S, 0, 1, ksize=3, scale=1, delta=0, borderType=cv.BORDER_DEFAULT)
    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)
    gmag = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    # Step 3 : Mark the foreground objects 
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (20, 20))
    Io = cv.morphologyEx(gray, cv.MORPH_OPEN, kernel)

    Ie = cv.erode(gray, kernel, 1)
    Iobr = reconstruction(Ie, gray)

    Ioc = cv.morphologyEx(Io, cv.MORPH_CLOSE, kernel)

    Iobrd = cv.dilate(Iobr, kernel, 1)
    Iobrcbr = reconstruction(imcomplement(Iobrd), cv.imcomplement(Iobr))
    Iobrcbr = cv.bitwise_not(Iobrcbr)


    # Step 4 : Compute background markers 
    # Step 5 : Compute the watershed transform of the segmentation function 
    # Step 6 : Visualize the result 
    # plt.subplot(121)
    # plt.imshow(cv.cvtColor(gray, cv.COLOR_BGR2RGB))
    # plt.title('Input')
    # plt.subplot(122)
    # plt.imshow(cv.cvtColor(Iobr, cv.COLOR_BGR2RGB))
    plt.imshow(Iobrcbr)
    plt.title('Output')

    plt.show()