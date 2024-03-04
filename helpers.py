import cv2 as cv
import mediapipe as mp
import os
import matplotlib.pyplot as plt
from vector_handler import *
from pyfirmata import Arduino, util, SERVO
from time import sleep
import serial
import serial.tools.list_ports


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

porta = None
board = None


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
    """Criar dicionário {"dedo/eixo": valor} para exportar pro arduino
    eixo vai ser separado em x, y, z
    x -> movimento horizontal do proximal
    y -> movimeto vertical do proximal
    z -> movimento vertical do medio
    """
    if not data:
        return
    
    # vetores referencia da palma
    vec0_1 = Vector3D(data[0], data[1]) #polegar
    vec0_5 = Vector3D(data[0], data[5]) #indicador
    vec0_9 = Vector3D(data[0], data[9]) #medio
    vec0_13 = Vector3D(data[0], data[13]) #anelar
    vec0_17 = Vector3D(data[0], data[17]) #minimo
    
    # vetores proximais (invertidos)
    vec2_1 = Vector3D(data[2], data[1]) #polegar
    vec6_5 = Vector3D(data[6], data[5]) #indicador
    vec10_9 = Vector3D(data[10], data[9]) #medio
    vec14_13 = Vector3D(data[14], data[13]) #anelar
    vec18_17 = Vector3D(data[18], data[17]) #minimo
    
    # vetores medios
    vec2_3 = Vector3D(data[2], data[3]) #polegar
    vec6_7 = Vector3D(data[6], data[7]) #indicador
    vec10_11 = Vector3D(data[10], data[11]) #medio
    vec14_15 = Vector3D(data[14], data[15]) #anelar
    vec18_19 = Vector3D(data[18], data[19]) #minimo
    
    #polegar
    MC1 = Bone("MC1", vec2_1, vec0_1)
    FP1 = Bone("FP1", vec2_3, vec2_1)
    
    #indicador
    FP2 = Bone("FP2", vec6_5, vec0_5)
    FM2 = Bone("FM2", vec6_7, vec6_5)
    
    #medio
    FP3 = Bone("FP3", vec10_9, vec0_9)
    FM3 = Bone("FM3", vec10_11,vec10_9)
    
    #anelar
    FP4 = Bone("FP4", vec14_13, vec0_13)
    FM4 = Bone("FM4", vec14_15, vec14_13)
    
    #minimo
    FP5 = Bone("FP5", vec18_17, vec0_17)
    FM5 = Bone("FM5", vec18_19, vec18_17)
    
    anglesDict = {
        "1/x": MC1.HAngle(), "1/y": MC1.VAngle(), "1/z" : FP1.VAngle(),
        "2/x": FP2.HAngle(), "2/y": FP2.VAngle(), "2/z" : FM2.VAngle(),
        "3/x": FP3.HAngle(), "3/y": FP3.VAngle(), "3/z" : FM3.VAngle(),
        "4/x": FP4.HAngle(), "4/y": FP4.VAngle(), "4/z" : FM4.VAngle(),
        "5/x": FP5.HAngle(), "5/y": FP5.VAngle(), "5/z" : FM5.VAngle(),
    }
    
    print(anglesDict)
    
    return anglesDict

def tryArduinoConect(port):
    try:
        global board
        board = Arduino(port)
        return True
    except:
        return False

def ArduinoInit():
    if not board:
        return
    it = util.Iterator(board)
    it.start()
    sleep(2)
    
    #void setup:
    global builtinled; builtinled = board.get_pin("d:13:o")

    board.digital[2].mode = SERVO
    board.digital[3].mode = SERVO
    board.digital[4].mode = SERVO
    pass

def executeArduino(anglesList : dict):
    #inserir
    #if not anglesList -> seta as posiçoes para default
    #depois de um timer (pesquisar como fazer)
    if not anglesList:
        return
    try:
        for angle in anglesList:
            if anglesList[angle] <= 0:
                anglesList[angle] = 0
            elif anglesList[angle] >= 180:
                anglesList[angle] = 180
        rotateServo(2, anglesList["2/z"])
        rotateServo(3, anglesList["3/z"])
        rotateServo(4, anglesList["4/z"])
    except:
        pass
    

def rotateServo(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.015)

def blink():
    print("blink")
    builtinled.write(1)
    sleep(.2)
    builtinled.write(0)
    sleep(.2)
    pass

def selectCom():
    while True:
        com_port = input("Digite a porta COM: ").upper()
        if tryArduinoConect(com_port):
            return com_port
        else:
            print(f"Erro ao conectar-se à porta {com_port}. Tente novamente.")

def comPorts():
    ports = serial.tools.list_ports.comports()
    
    if not ports:
        print("Nenhuma porta COM encontrada.")
    else:
        print("Portas COM disponíveis:")
        for port in ports:
            print(f"    {port.device} ---> {port.description}")

def programInit():
    sleep(1)
    print("Iniciando Programa")
    sleep(1)
    print("Bem vindo!")
    sleep(0.5)
    print("Escolha em qual porta onde o dispositivo esteja conectado.")
    
    comPorts()
    selectCom()
    
    ArduinoInit()

    print("conectado!")
    sleep(2)
    print('Camera ligando em')
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(1)
        
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


