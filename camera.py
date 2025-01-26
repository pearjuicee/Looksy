import os

import cvzone
import cv2
from cvzone.PoseModule import PoseDetector
import numpy as np

# cap = cv2.VideoCapture("Resources/Videos/1.mp4")
cap = cv2.VideoCapture(0)
detector = PoseDetector()

# cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
# cv2.setWindowProperty("Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1440)

# Get actual dimensions
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(f"Width: {width}")
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"Height: {height}")

# Adjust button positions based on actual dimensions
button_right_x = int(width * 0.8)  # 80% of width
button_left_x = int(width * 0.1)   # 20% of width

button_y = 300

shirtFolderPath = "Resources/Shirts"
listShirts = os.listdir(shirtFolderPath)
# print(listShirts)
fixedRatio = 262 / 190  # widthOfShirt/widthOfPoint11to12
shirtRatioHeightWidth = 581 / 440
imageNumber = 0
imgButtonRight = cv2.imread("./Resources/button.png", cv2.IMREAD_UNCHANGED)
imgButtonLeft = cv2.flip(imgButtonRight, 1)
counterRight = 0
counterLeft = 0
selectionSpeed = 10

def generate_frames():
    global imageNumber, counterRight, counterLeft
    while True:
        success, img = cap.read()
        img = detector.findPose(img, draw=False)
        # img = cv2.flip(img,1)
        lmList, bboxInfo = detector.findPosition(img, draw=False)
        if lmList:
            # center = bboxInfo["center"]
            lm11 = lmList[11][1:3]
            lm12 = lmList[12][1:3]
            imgShirt = cv2.imread(os.path.join(shirtFolderPath, listShirts[imageNumber]), cv2.IMREAD_UNCHANGED)

            widthOfShirt = abs(int((lm11[0] - lm12[0]) * fixedRatio))
            print(widthOfShirt)
            imgShirt = cv2.resize(imgShirt, (widthOfShirt, int(widthOfShirt * shirtRatioHeightWidth)))
            currentScale = (lm11[0] - lm12[0]) / 190
            offset = int(44 * currentScale), int(48 * currentScale)

            try:
                img = cvzone.overlayPNG(img, imgShirt, (lm12[0] - offset[0], lm12[1] - offset[1]))
            except:
                pass
                    
            img = cvzone.overlayPNG(img, imgButtonRight, (button_right_x, button_y))
            img = cvzone.overlayPNG(img, imgButtonLeft, (button_left_x, button_y))

            ellipse_offset = 66
            if lmList[16][1] < 300:
                counterRight += 1
                cv2.ellipse(img, (button_left_x + ellipse_offset, button_y + ellipse_offset), 
                            (66, 66), 0, 0, counterRight * selectionSpeed, (0, 255, 0), 20)
                if counterRight * selectionSpeed > 360:
                    counterRight = 0
                    if imageNumber < len(listShirts) - 1:
                        imageNumber += 1
            elif lmList[15][1] > 900:
                counterLeft += 1
                cv2.ellipse(img, (button_right_x + ellipse_offset, button_y + ellipse_offset), 
                            (66, 66), 0, 0, counterLeft * selectionSpeed, (0, 255, 0), 20)
                if counterLeft * selectionSpeed > 360:
                    counterLeft = 0
                    if imageNumber > 0:
                        imageNumber -= 1

            else:
                counterRight = 0
                counterLeft = 0

        _, buffer = cv2.imencode('.jpg', img)
        array_np = np.array(buffer)
        frame = array_np.tobytes()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')