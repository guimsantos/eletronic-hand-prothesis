import helpers as hp
import os

debugMode = True

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
            hp.VectorsToAngles(handPoints)
            try:
                print(handPoints[8])
            except:
                pass
            #print(handPoints)
            hp.blink()


if __name__ == "__main__":
    main()
