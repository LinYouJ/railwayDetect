import cv2
import numpy as np

def maskROI(img):
    coordinate = np.array([[0, img.shape[0]], [295, 100], [402, 95], [img.shape[1], img.shape[0]]])
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, [coordinate], (255, 255, 255))
    mask_img = cv2.bitwise_and(img, mask)
    return mask_img, mask

while True: 
    oriImg = cv2.imread(r'railwayDist/railway.png')
    Img = cv2.resize(oriImg, (700, 500))
    imgGray = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0, 0)
    imgCan = cv2.Canny(imgBlur, 171, 57)

    imgMask, mask = maskROI(imgCan)

    #cv2.imshow('img', Img)
    #cv2.imshow('imgCan', imgCan)
    cv2.imshow('mask', imgMask)
    cv2.imshow('imgmask', mask)
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break
