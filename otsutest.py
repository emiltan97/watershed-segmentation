import cv2 as cv
from matplotlib import pyplot as plt

def convertBlackPxToWhitePx (img) : 
    for i in range(0, img.shape[0]) : 
        for j in range(1, img.shape[1]) : 
            pixel = img[i][j]
            if not pixel[:3].any() : 
                img[i][j] = [255, 255, 255]

    return img

if __name__ == "__main__" : 
    inp = cv.imread('data/02.png')
    # img = convertBlackPxToWhitePx(inp)
    img = cv.cvtColor(inp, cv.COLOR_BGR2GRAY)
    
    # global thresholding
    ret1,th1 = cv.threshold(img, 150,255,cv.THRESH_BINARY_INV)

    # Otsu's thresholding
    ret2,th2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

    # Otsu's thresholding after Gaussian filtering
    blur = cv.GaussianBlur(img,(5,5),0)
    ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
    
    plt.subplot(221)
    plt.imshow(cv.cvtColor(inp, cv.COLOR_BGR2RGB))
    plt.title('input')
    plt.subplot(222)
    plt.imshow(cv.cvtColor(th1, cv.COLOR_BGR2RGB))
    plt.title('global')
    plt.subplot(223)
    plt.imshow(cv.cvtColor(th2, cv.COLOR_BGR2RGB))
    plt.title('otsu')
    plt.subplot(224)
    plt.imshow(cv.cvtColor(th3, cv.COLOR_BGR2RGB))
    plt.title('otsu after gaussian')

    plt.show()

