import cv2
import numpy as np

ori_cor = [[255, 159], [457, 158], [663, 473], [40, 464]]
xy_tran = [[159, 255], [158, 457], [473, 663], [464, 40]]

def nothing():
    pass

def initTrackbars():
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 300, 100)
    cv2.createTrackbar("Threshold1", "Trackbars", 100, 255, nothing)
    cv2.createTrackbar("Threshold2", "Trackbars", 100, 255, nothing)

def valTrackbars(): 
    Threshold1 = cv2.getTrackbarPos("Threshold1", "Trackbars")
    Threshold2 = cv2.getTrackbarPos("Threshold2", "Trackbars")
    return [Threshold1, Threshold2]

def TopView(Img):
    p1 = np.float32([[255, 159], [457, 158], [663, 473], [40, 464]])
    p2 = np.float32([[0, 0], [500, 0], [500, 700], [0, 700]])
    Matrix = cv2.getPerspectiveTransform(p1, p2)
    output = cv2.warpPerspective(Img, Matrix, (img.shape[0], img.shape[1]))
    cv2.imshow('out', output)
    
initTrackbars()
while True:
    
    img = cv2.imread(r'railwayDist/railway.png')
    img = cv2.resize(img, (700, 500))
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # result = valTrackbars()
    # imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0, 0)
    # Image = cv2.Canny(imgBlur, result[0], result[1])

    #cv2.imshow('Img', Image)
    coordinate = [[257, 144], [437, 135], [666, 479], [35, 475]]
    cv2.line(img, coordinate[0], coordinate[1], (0, 0, 255), 2)
    cv2.line(img, coordinate[1], coordinate[2], (0, 0, 255), 2)
    cv2.line(img, coordinate[2], coordinate[3], (0, 0, 255), 2)
    cv2.line(img, coordinate[3], coordinate[0], (0, 0, 255), 2)

    TopView(img)
    cv2.imshow('img', img)
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break

