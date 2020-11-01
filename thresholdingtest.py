import cv2 as cv
import numpy as np  

from matplotlib import pyplot as plt

def convertBlackPxToWhitePx (img) : 
    for i in range(0, img.shape[0]) : 
        for j in range(1, img.shape[1]) : 
            pixel = img[i][j]
            if not pixel[:3].any() : 
                img[i][j] = [255, 255, 255]

    return img

if __name__ == "__main__" : 
    # Read the image 
    img = cv.imread('data/02.png')
    # img = convertBlackPxToWhitePx(img)
    # plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    # plt.show()
    # img = cv.bitwise_not(img)
    # Resize the image to 500 by 500 pixels 
    resized = cv.resize(img, (500, 500))
    # Perform a median blur with a window of 5 by 5 pixels 
    blurred = cv.medianBlur(img, 5)
    # Perform k nearest neighbors (kNN) clustering on the colors of the images 
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 7
    temp = blurred.reshape((blurred.shape[0] * blurred.shape[1], 3))
    # temp = np.transpose(temp, (1, 0))
    temp = np.float32(temp)
    ret,label,center=cv.kmeans(temp,K,None,criteria,10,cv.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    res1 = center[label.flatten()]
    # Take the gray scale of the image
    res1 = res1.reshape((blurred.shape))
    grayscale = cv.cvtColor(res1, cv.COLOR_BGRA2GRAY)
    # Perform a median blur with a window of 9 by 9 pixels 
    blurred2 = cv.medianBlur(grayscale, 9)
    # Perform kNN clustering on the colors of the images 
    temp2 = blurred2.reshape((blurred2.shape[0] * blurred2.shape[1]), -1)
    temp2 = np.float32(blurred2)
    K = 4
    ret,label,center=cv.kmeans(temp2,K,None,criteria,100,cv.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    res2 = center[label.flatten()]
    res2 = res2.reshape((blurred2.shape))
    # Perform a binary invert threshold filter on the image with a threshold of 200 
    ret,th = cv.threshold(grayscale,127,255,cv.THRESH_BINARY)

    # plt.subplot(421)
    # plt.imshow(cv.cvtColor(img, cv.COLOR_BGRA2RGBA))
    # plt.title('input')
    # plt.subplot(422)
    # plt.imshow(cv.cvtColor(resized, cv.COLOR_BGRA2RGBA))
    # plt.title('resized')
    # plt.subplot(423)
    # plt.imshow(cv.cvtColor(blurred, cv.COLOR_BGRA2RGBA))
    # plt.title('blurred')
    # plt.subplot(424)
    # plt.imshow(cv.cvtColor(res1, cv.COLOR_BGRA2RGBA))
    # plt.title('first knn')
    # plt.subplot(425)
    # plt.imshow(cv.cvtColor(grayscale, cv.COLOR_BGRA2RGBA))
    # plt.title('grayscale')
    # plt.subplot(426)
    # plt.imshow(cv.cvtColor(blurred2, cv.COLOR_BGRA2RGBA))
    # plt.title('second blurred')
    # plt.subplot(427)
    # plt.imshow(cv.cvtColor(res2, cv.COLOR_BGRA2RGBA))
    # plt.title('second knn')
    # plt.subplot(428)
    # plt.imshow(cv.cvtColor(th, cv.COLOR_BGRA2RGBA))
    # plt.title('threshold')

    plt.imshow(cv.cvtColor(th, cv.COLOR_BGR2RGB))

    plt.show()

