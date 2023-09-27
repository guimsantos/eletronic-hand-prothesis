import cv2 as cv
import mediapipe as mp
import os

video = cv.VideoCapture(0)

hands = mp.solutions.hands
Hand = hands.Hands(max_num_hands=1)

mpDraw = mp.solutions.drawing_utils

while True:
    check, img = video.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = Hand.process(imgRGB)
    handPoints = results.multi_hand_landmarks
    h,w,_ = img.shape
    if handPoints:
        for points in handPoints:
            #print(points)
            mpDraw.draw_landmarks(img, points,hands.HAND_CONNECTIONS)
            for id, cord in enumerate(points.landmark):
                cx, cy, cz = int(cord.x * w), int(cord.y * h), cord.z
                cv.putText(img, str(id), (cx, cy + 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                
                if id == 6:
                    refIndicador = (cx, cy)
                    
                if id == 8:
                    os.system('cls')
                    print(f'ID: {id}')
                    print(f'x: {cx}')
                    print(f'y: {cy}')
                    print(f'z: {cz}')
                    if cy > refIndicador[1]:
                        print("Indicador Abaixado")
                    else:
                        print("Indicador Levantado")
                
    
                
                
    cv.imshow("Hand Position Detection", img)
    cv.waitKey(1)
