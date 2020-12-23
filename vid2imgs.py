import cv2
vidcap = cv2.VideoCapture('pi2.mp4')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("D:\\projects\\dataset\\pigeon\\"+"pigeon"+str(count)+".jpg", image)
        #print("saved")
    return hasFrames
sec = 0
frameRate = 0.8
count=10000
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
    print(count)