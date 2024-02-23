import helpers as hp
import os

debugMode = True

handPoints = []

def main():
    if debugMode:
        print("Debug Mode Started")
        hp.programInit()
        while True:
            hp.blink()
        
        
    else:
        while True:
            handPoints = hp.movementCapture()
            #hp.plot3D(handPoints)
            os.system('cls')
            hp.VectorsToAngles(handPoints)
            print(handPoints)
                

if __name__ == "__main__":
    main()
