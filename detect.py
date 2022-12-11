import cv2

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

initTrackbars()
while True:
    
    img = cv2.imread(r'railwayDist/railway.png')
    img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    result = valTrackbars()
    _, imgTh = cv2.threshold(imgGray, result[0], result[1], cv2.THRESH_BINARY_INV)
    #imgCan = cv2.Canny(imgGray, 100, 230)
    #Img = cv2.GaussianBlur(imgCan, (5, 5), 0)
    Img = cv2.erode(imgTh, (7,7), iterations=5)
    Img = cv2.dilate(Img, (3, 3), iterations=3)

    contours, hieracht = cv2.findContours(imgTh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for ctr in contours:
        if cv2.contourArea(ctr) > 1000:
            cv2.drawContours(img, ctr, -1, (0, 255, 255), 2)

    # Img = cv2.dilate(Img, (3, 3), iterations=5)
    # Img = cv2.erode(Img, (3, 3), iterations=5)
    #cv2.imshow('imgCan', imgCan)
    cv2.imshow('Img', Img)
    cv2.imshow('img', img)

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break