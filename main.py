import helpers as hp
import os

handPoints = []

def main():
    while True:
        handPoints = hp.movementCapture()
        #hp.plot3D(handPoints)
        os.system('cls')
        hp.VectorsToAngles(handPoints)
        print(handPoints)
                

if __name__ == "__main__":
    main()
