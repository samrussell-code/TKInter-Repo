from math import *

class Physics():
    force=0
    mass=0
    acceleration=0
    initial_velocity=0
    initial_velocity=0
    distance=0
    time=0
    magnitude=0

    def VectorMagnitude(self,i,j,k=0):
        self.ModifyValues(magnitude=sqrt((i**2)+(j**2)+(k**2)))

    def ModifyValues(self,**variables):
        for key, value in variables.items():
            setattr(self, key, value)

#rect_phy=Physics()
#rect_phy.ModifyValues(mass=5,acceleration=7)
#rect_phy.VectorMagnitude(2,5)
#print(rect_phy.magnitude)