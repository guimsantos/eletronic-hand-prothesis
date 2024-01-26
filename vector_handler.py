import math

class Vector3D:
    def __init__(self, fPoint : tuple, sPoint : tuple):
        self.x = sPoint[0] - fPoint[0]
        self.y = sPoint[1] - fPoint[1]
        self.z = sPoint[2] - fPoint[2]


class Bone:
    def __init__(self, boneName : str, boneVec0 : tuple, boneVec1 : tuple, refVec0: tuple, refVec1 : tuple):
        self.boneVec : Vector3D = Vector3D(boneVec0, boneVec1)
        self.refVec : Vector3D = Vector3D(refVec0, refVec1)
        self.name : str = boneName
        self.Vangle : float
        self.Hangle : float

    def Angle3D(self):
        # produto escalar entre bone e ref
        axb = self.boneVec.x * self.refVec.x + self.boneVec.y * self.refVec.y + self.boneVec.z * self.refVec.z
        aCatSqr = float((self.boneVec.z) ** 2 + (self.boneVec.y) ** 2 + (self.boneVec.z) ** 2)
        bCatSqr = float((self.refVec.z) ** 2 + (self.refVec.y) ** 2) + (self.boneVec.z) ** 2

        # magnetudes dos dois vetores
        aMag = math.sqrt(math.fabs(aCatSqr))
        bMag = math.sqrt(math.fabs(bCatSqr))
        
        # calculo do angulo
        print(axb/(aMag * bMag))   
        if (aMag * bMag) != 0:
            
            frac = axb/(aMag * bMag)
            if frac > 1:
                frac = 1
            elif frac < -1:
                frac = -1

            radAngle = math.acos(frac)
            angleAB = math.degrees(radAngle)
            self.VAngle = angleAB
            
            print(self.name)
            print(f"escalar {axb}")
            print(f"magnetude {aMag}")
            print(f"cos angulo V {axb/(aMag * bMag)}")        
            print(f"angulo V {angleAB}")
        

    def VAngle(self):
        # produto escalar entre bone e ref
        axb = self.boneVec.z * self.refVec.z + self.boneVec.y * self.refVec.y
        
        # magnetudes dos dois vetores
        aCatSqr = float((self.boneVec.z) ** 2 + (self.boneVec.y) ** 2)
        bCatSqr = float((self.refVec.z) ** 2 + (self.refVec.y) ** 2)
        aMag = math.sqrt(math.fabs(aCatSqr))
        bMag = math.sqrt(math.fabs(bCatSqr))
        
        # calculo do angulo
        if (aMag * bMag) != 0:
            
            frac = axb/(aMag * bMag)
            if frac > 1:
                frac = 1
            elif frac < -1:
                frac = -1
                
            radAngle = math.acos(frac)
            angleAB = math.degrees(radAngle)
            self.VAngle = angleAB
            
            print(self.name)
            print(f"escalar {axb}")
            print(f"magnetude {aMag}")
            print(f"cos angulo V {axb/(aMag * bMag)}")        
            print(f"angulo V {angleAB}")
            return angleAB
        

    def HAngle(self):
        # produto escalar entre bone e ref
        axb = self.boneVec.x * self.refVec.x + self.boneVec.y * self.refVec.y
        
        # magnetudes dos dois vetores
        aCatSqr = float((self.boneVec.x) ** 2 + (self.boneVec.y) ** 2)
        bCatSqr = float((self.refVec.x) ** 2 + (self.refVec.y) ** 2)
        aMag = math.sqrt(math.fabs(aCatSqr))
        bMag = math.sqrt(math.fabs(bCatSqr))
        
        # calculo do angulo
        if (aMag * bMag) != 0:
            
            frac = axb/(aMag * bMag)
            if frac > 1:
                frac = 1
            elif frac < -1:
                frac = -1
                
            radAngle = math.acos(frac)
            angleAB = math.degrees(radAngle)
            self.VAngle = angleAB
            
            print(self.name)
            print(f"escalar {axb}")
            print(f"magnetude {aMag}")
            print(f"cos angulo H {axb/(aMag * bMag)}")        
            print(f"angulo H {angleAB}")
            return angleAB
    
        
        