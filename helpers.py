import cv2 as cv
import mediapipe as mp
import os
import matplotlib.pyplot as plt
from vector_handler import *

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


lastPoints = []

video = cv.VideoCapture(0)
hands = mp.solutions.hands
Hand = hands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

def movementCapture():
    pointsList = []
        
    check, img = video.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = Hand.process(imgRGB)
    handPoints = results.multi_hand_landmarks
    h,w,_ = img.shape

    if handPoints:
        for points in handPoints:
            mpDraw.draw_landmarks(img, points,hands.HAND_CONNECTIONS)
            
            for id, cord in enumerate(points.landmark):
                cx, cy, cz = int(cord.x * w), int(cord.y * h), int(cord.z * h)
                pointsList.append((cx, cy, cz))

    cv.imshow("Maozinha SENAI 2000 Pro Max", img)
    cv.waitKey(1)
    return pointsList

def VectorsToAngles(data : list):
    """Criar dicionário {"dedo/eixo": valor} para exportar pro arduino"""
    if not data:
        return
    
    vec0 = Vector3D(data[5], data[0])
    vec1 = Vector3D(data[5], data[6])
    vec2 = Vector3D(data[7], data[6])
    
    fp2 = Bone("FP_2", data[5], data[6], data[5], data[0])
    fm2 = Bone("FM_2", data[7], data[6], data[5], data[6])
    
    fp2.VAngle()
    fp2.HAngle()
    
    

def plot3D(data : list):    
    if not data:
        return
    
    ax.clear()

    x, y, z = zip(*data)

    ax.scatter(x, z, y, c='r', marker='o')
    
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.set_zlabel('Eixo Z')
    os.system('cls')
    print(data)
    plt.draw()
    plt.pause(0.2)
        
def executeArduino(processedData : list):
    pass