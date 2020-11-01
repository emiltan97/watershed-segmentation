import cv2 as cv
from matplotlib import pyplot as plt

if __name__ == "__main__" : 
    img = cv.imread('data/01.png')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    kernel1 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (20, 20))
    res1 = cv.morphologyEx(gray, cv.MORPH_OPEN, kernel1)
    kernel2 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (10, 10))
    res2 = cv.morphologyEx(gray, cv.MORPH_OPEN, kernel2)
    kernel3 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
    res3 = cv.morphologyEx(gray, cv.MORPH_OPEN, kernel3)
    kernel4 = cv.getStructuringElement(cv.MORPH_RECT, (20, 20))
    res4 = cv.morphologyEx(gray, cv.MORPH_OPEN, kernel4)

    plt.subplot(221)
    plt.imshow(cv.cvtColor(res1, cv.COLOR_BGR2RGB))
    plt.title('20')
    plt.subplot(222)
    plt.imshow(cv.cvtColor(res2, cv.COLOR_BGR2RGB))
    plt.title('10')
    plt.subplot(223)
    plt.imshow(cv.cvtColor(res3, cv.COLOR_BGR2RGB))
    plt.title('5')
    plt.subplot(224)
    plt.imshow(cv.cvtColor(res4, cv.COLOR_BGR2RGB))
    plt.title('rect')

    plt.show()
