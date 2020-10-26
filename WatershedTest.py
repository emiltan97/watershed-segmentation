# import numpy as np 
# import cv2 as cv 

# from matplotlib import pyplot as plt 

# img = cv.imread('data/04.jpg') 
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
# ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU) 
# # noise removal
# kernel = np.ones((3,3),np.uint8)
# opening = cv.morphologyEx(thresh,cv.MORPH_OPEN,kernel, iterations = 2)
# # sure background area
# sure_bg = cv.dilate(opening,kernel,iterations=3)
# # Finding sure foreground area
# dist_transform = cv.distanceTransform(opening,cv.DIST_L2,5)
# ret, sure_fg = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)
# # Finding unknown region
# sure_fg = np.uint8(sure_fg)
# unknown = cv.subtract(sure_bg,sure_fg)
# # Marker labelling
# ret, markers = cv.connectedComponents(sure_fg)
# # Add one to all labels so that sure background is not 0, but 1watere
# markers = markers+1
# # Now, mark the region of unknown with zero
# markers[unknown==255] = 0
# markers = cv.watershed(img,markers)
# img[markers == -1] = [255,0,0]

# plt.subplot(211)
# plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
# plt.title('Input')
# plt.subplot(212)
# plt.imshow(cv.cvtColor(thresh, cv.COLOR_BGR2RGB))
# plt.title('Thresh')

# plt.show()



# import cv2
# import numpy as np
# from skimage.feature import peak_local_max
# from skimage.morphology import watershed
# from scipy import ndimage

# # Load in image, convert to gray scale, and Otsu's threshold
# image = cv2.imread('data/04.jpg')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# # Compute Euclidean distance from every binary pixel
# # to the nearest zero pixel then find peaks
# distance_map = ndimage.distance_transform_edt(thresh)
# local_max = peak_local_max(distance_map, indices=False, min_distance=20, labels=thresh)

# # Perform connected component analysis then apply Watershed
# markers = ndimage.label(local_max, structure=np.ones((3, 3)))[0]
# labels = watershed(-distance_map, markers, mask=thresh)

# # Iterate through unique labels
# total_area = 0
# for label in np.unique(labels):
#     if label == 0:
#         continue

#     # Create a mask
#     mask = np.zeros(gray.shape, dtype="uint8")
#     mask[labels == label] = 255

#     # Find contours and determine contour area
#     cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     cnts = cnts[0] if len(cnts) == 2 else cnts[1]
#     c = max(cnts, key=cv2.contourArea)
#     area = cv2.contourArea(c)
#     total_area += area
#     cv2.drawContours(image, [c], -1, (36,255,12), 4)

# # plt.subplot(211)
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.title('Input')
# # plt.subplot(212)
# # plt.imshow(cv.cvtColor(thresh, cv.COLOR_BGR2RGB))
# # plt.title('Thresh')

# plt.show()