import cv2
import numpy as np

def GET_COORDINATES():
    img = cv2.imread(r'railwayDist/railway.png')
    img = cv2.resize(img, (700, 500))
    def OnMouseDown(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            xy = "%d, %d" % (x, y)
            print(xy)
            cv2.circle(img, (x, y), 1, (255, 0, 0), thickness=-1)
            cv2.putText(img, xy,(x, y), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), thickness=1)
            #cv2.imshow('img', img)
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", OnMouseDown)
    cv2.imshow("image", img)
    if cv2.waitKey(0) == ord('q'):
        cv2.destroyAllWindows() 

def TopView():
    img = cv2.imread(r'railwayDist/railway.png')
    img = cv2.resize(img, (700, 500))
    p1 = np.float32([[257, 144], [437, 135], [666, 479], [35, 475]])
    p2 = np.float32([[0, 0], [700, 0], [700, 500], [0, 500]])
    Matrix = cv2.getPerspectiveTransform(p1, p2)
    output = cv2.warpPerspective(img, Matrix, (img.shape[1], img.shape[0]))
    cv2.imshow('out', output)
    if cv2.waitKey(0) == ord('q'):
        cv2.destroyAllWindows()


class TrackBar():
    def __init__(self):
        cv2.namedWindow("Trackbars")
        cv2.resizeWindow("Trackbars", 300, 100)
        cv2.createTrackbar("Threshold1", "Trackbars", 100, 255, self.nothing)
        cv2.createTrackbar("Threshold2", "Trackbars", 100, 255, self.nothing)

    def nothing(self):
        pass        

    def valTrackbars(self): 
        self.Threshold1 = cv2.getTrackbarPos("Threshold1", "Trackbars")
        self.Threshold2 = cv2.getTrackbarPos("Threshold2", "Trackbars")
        return [self.Threshold1, self.Threshold2]

def testImg():
    Bar = TrackBar()
    while True:
        oriImg = cv2.imread(r'railwayDist/railway.png')
        Img = cv2.resize(oriImg, (700, 500))
        imgGray = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0, 0)
        result =Bar.valTrackbars()
        imgCan = cv2.Canny(imgBlur, result[0], result[1])
        cv2.imshow('imgBlur', imgBlur)
        cv2.imshow('imgCan', imgCan)
        print(result[0], result[1])

        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()



if __name__ == "__main__":
    #TopView()
    GET_COORDINATES()
    #testImg()

