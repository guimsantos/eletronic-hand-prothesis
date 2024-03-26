import helpers as hp
import os
from time import sleep

debugMode = False

handPoints = []

def main():
    if debugMode:
        hp.programInit()
        while True:
            hp.executeArduino({})
        
    else:
        hp.programInit()
        while True:
            handPoints = hp.movementCapture()
            #hp.plot3D(handPoints)
            os.system('cls')
            boneAngles = hp.VectorsToAngles(handPoints)
            hp.executeArduino(boneAngles)
            sleep(0.05)


if __name__ == "__main__":
    main()
