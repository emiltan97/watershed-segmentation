import cv2 as cv
import numpy as np  

from matplotlib import pyplot as plt

def filterLabelNum(stat, labelNum, minSize) :

    filteredLabelNum = []

    sizes = stat[1:, -1]

    for i in range(1, labelNum) :
        if sizes[i-1] >= minSize : 
            filteredLabelNum.append(i)

    return filteredLabelNum

def computeCCL(labelNum, label):
    for i in range(0, len(label)) :
        for j in range(0, len(label[i])) :
            if label[i][j] not in labelNum :
                label[i][j] = 0

    labelCol = np.uint8(255 * label/np.max(label))
    blankCol = 255 * np.ones_like(labelCol)
    ccl      = cv.merge([labelCol, blankCol, blankCol])
    ccl[labelCol == 0] = 0 

    return ccl

def module1(img) : 

    kr = 0.2989 
    kg = 0.5870 
    kb = 0.1140

    for i in range(0, img.shape[0]) : 
        for j in range(1, img.shape[1]) : 
            pixel = img[i][j] 
            pixel = [
                pixel[0] * kb + 
                pixel[1] * kg + 
                pixel[2] * kr
            ] 
            img[i][j] = pixel

    return img

def module3(img) : 
    # Connected Components Labelling 
    labelNum, label, stat, centroid = cv.connectedComponentsWithStats(img, 8)
    # Discard small connected components 
    filteredLabelNum = filterLabelNum(stat, labelNum, 2500)
    # Compute CCL image
    ccl = computeCCL(filteredLabelNum, label)
    # Closing 
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (7, 7))
    closing = cv.morphologyEx(ccl, cv.MORPH_CLOSE, kernel)

    return closing

if __name__ == "__main__" : 
    # Read the colored image
    img = cv.imread('sample.png')
    # Resize the image to 500 by 500 pixels 
    resized = cv.resize(img, (500, 500))
    # Computation of a high contrast monochrome image 
    res1 = module1(resized)
    res1 = cv.cvtColor(res1, cv.COLOR_BGR2GRAY)
    # Global threshold estimation 
    ret, res2 = cv.threshold(res1, 150, 255, cv.THRESH_BINARY)
    # Morphological operation 
    # noise removal
    kernel = np.ones((3,3),np.uint8)
    opening = cv.morphologyEx(res2,cv.MORPH_OPEN,kernel, iterations = 2)
    # sure background area
    sure_bg = cv.dilate(opening,kernel,iterations=3)
    # Finding sure foreground area
    dist_transform = cv.distanceTransform(opening,cv.DIST_L2,5)
    ret, sure_fg = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)
    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv.subtract(sure_bg,sure_fg)
    # res3 = module3(res2)
    # res3 = cv.cvtColor(res3, cv.COLOR_BGR2GRAY)
    # Watershed segmentation 
    # Marker labelling
    ret, markers = cv.connectedComponents(sure_fg)
    # Add one to all labels so that sure background is not 0, but 1
    markers = markers+1
    # Now, mark the region of unknown with zero
    markers[unknown==255] = 0
    markers = cv.watershed(resized,markers)
    resized[markers == -1] = [255,0,0]
    # Displaying results
    plt.subplot(221)
    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    plt.title('Input')
    plt.subplot(222) 
    plt.imshow(cv.cvtColor(res1, cv.COLOR_BGR2RGB))
    plt.title('Mod 1')
    plt.subplot(223)
    plt.imshow(cv.cvtColor(res2, cv.COLOR_BGR2RGB))
    plt.title('Mod 2')
    plt.subplot(224)
    plt.imshow(resized)
    plt.title('Mod 3')

    plt.show() 