import cv2
import numpy as np

def maskROI(img):
    coordinate = np.array([[0, img.shape[0]], [295, 100], [402, 95], [img.shape[1], img.shape[0]]])
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, [coordinate], (255, 255, 255))
    mask_img = cv2.bitwise_and(img, mask)
    return mask_img, mask
    

oriImg = cv2.imread('railway.png')
Img = cv2.resize(oriImg, (700, 500))
imgGray = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0, 0)
imgCan = cv2.Canny(imgBlur, 171, 57)

imgMask, mask = maskROI(imgCan)

Lines = cv2.HoughLinesP(imgMask, 1, np.pi/180, 100, minLineLength=100, maxLineGap=6)
for line in Lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(Img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    m = (y2 - y1)/(x2 - x1)
    if m > 0:
        print(f'left:{m}')
    else :
        print(f'right:{m}')

cv2.imshow('mask', imgMask)
cv2.imshow('Img', Img)

if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()
        
    