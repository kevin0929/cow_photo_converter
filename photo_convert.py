import cv2 as cv 

def video_demo():
    capture = cv.VideoCapture("video1.mp4")
    flag = 1
    name_label = 2237
    while True:
        ret, frame = capture.read()
        #cv.imshow("frame", frame)
        if (flag % 60 == 0) and (ret is True):
            cv.imshow("frame", frame)
            cv.imwrite("img/" + str(name_label) + ".png", frame)
            name_label = name_label + 1
        flag = flag + 1
        if cv.waitKey(100) & 0xFF == ord('q'):
            break

video_demo()
cv.destroyAllWindows()