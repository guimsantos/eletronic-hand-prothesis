import helpers as hp
import os

debugMode = False

handPoints = []

def main():
    if debugMode:
        print("Debug Mode Started")
        #hp.ArduinoInit()
        #hp.executeArduino()
    
    else:
        while True:
            handPoints = hp.movementCapture()
            #hp.plot3D(handPoints)
            os.system('cls')
            hp.VectorsToAngles(handPoints)
            print(handPoints)
                

if __name__ == "__main__":
    main()
