import numpy as np
import cv2
import utlis

cameraFeed= False
videoPath = 'VideoTest01.mp4'
cameraNo= 0
frameWidth= 540
frameHeight = 405
if cameraFeed:intialTracbarVals = [24,55,12,100] #  #wT,hT,wB,hB
else:intialTracbarVals =[37,62,2,87]#hT,wB,hB

####################################################

if cameraFeed:
    cap = cv2.VideoCapture(cameraNo)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
else:
    cap = cv2.VideoCapture(videoPath)
count=0
noOfArrayValues =10
global arrayCurve, arrayCounter
arrayCounter=0
arrayCurve = np.zeros([noOfArrayValues])
myVals=[]
utlis.initializeTrackbars(intialTracbarVals)


while True:

    success, img = cap.read()
    #img= cv2.imread('imag.jpg')
    if cameraFeed== False:img = cv2.resize(img, (frameWidth, frameHeight), None)
    imgWarpPoints = img.copy()
    imgFinal = img.copy()
    imgCanny = img.copy()

    imgUndis = utlis.undistort(img)
    imgThres,imgCanny,imgColor = utlis.thresholding(imgUndis)
    src = utlis.valTrackbars()
    imgWarp = utlis.perspective_warp(imgThres, dst_size=(frameWidth, frameHeight), src=src)
    imgWarpPoints = utlis.drawPoints(imgWarpPoints, src)
    imgSliding, curves, lanes, ploty = utlis.sliding_window(imgWarp, draw_windows=True)

    try:
        curverad =utlis.get_curve(imgFinal, curves[0], curves[1])
        lane_curve = np.mean([curverad[0], curverad[1]])
        imgFinal = utlis.draw_lanes(img, curves[0], curves[1],frameWidth,frameHeight,src=src)
        center = curverad[2]
        print(center)
        # ## Average
        currentCurve = lane_curve // 50
        if  int(np.sum(arrayCurve)) == 0:averageCurve = currentCurve
        else:
            averageCurve = np.sum(arrayCurve) // arrayCurve.shape[0]
        if abs(averageCurve-currentCurve) >200: arrayCurve[arrayCounter] = averageCurve
        else :arrayCurve[arrayCounter] = currentCurve
        arrayCounter +=1
        if arrayCounter >=noOfArrayValues : arrayCounter=0
        cv2.putText(imgFinal, str("Centru {0:.2f} m").format(float(center*10)), (frameWidth//10-10, 50), cv2.FONT_HERSHEY_TRIPLEX , 1.75, (126, 150, 190), 2, cv2.LINE_AA)
        cv2.putText(imgFinal, str("Curbura {0} m").format(int(lane_curve), int(lane_curve)),\
                    (frameWidth // 10 - 10, 100), cv2.FONT_HERSHEY_DUPLEX, 1.75, (126, 150, 190), 2, cv2.LINE_AA)

    except:
        lane_curve=00
        pass

    imgFinal= utlis.drawLines(imgFinal,lane_curve)
    #imgFinal= utlis.textDisplay(lane_curve,imgFinal)
    print("img shape {0}",int(imgFinal.shape[1]))
    imgThres = cv2.cvtColor(imgThres,cv2.COLOR_GRAY2BGR)
    imgBlank = np.zeros_like(img)
    """
    cv2.imshow("original",img)
    cv2.imshow("calibrare", imgUndis)
    cv2.imshow("filtru COLOR", imgColor)
    cv2.imshow("Filtru Canny", imgCanny)
    cv2.imshow("Canny + COLOR", imgThres)
    cv2.imshow("Regiune de Interes", imgWarpPoints)
    cv2.imshow("Imagine Perspectiva", imgWarp)
    cv2.imshow("Algoritmul ferestrelor glisante", imgSliding)
    cv2.imshow("Imagine Finala", imgFinal)
    """

    imgStacked = utlis.stackImages(0.7, ([img,imgUndis,imgColor,imgCanny],
                                        [imgThres,imgWarpPoints, imgWarp,imgSliding],
                                         ))

    cv2.imshow("Flux de lucru",imgStacked)
    cv2.imshow("Imagine finala", imgFinal)
    cv2.imshow("Algoritm ferestre glisante", imgSliding)
   # plt.plot(utlis.get_hist(imgWarp))
   # plt.show()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  # time.sleep(0.09)
cap.release()
cv2.destroyAllWindows()
