from math import *

class Physics():
    force=0
    mass=0
    acceleration=0
    initial_velocity=0
    final_velocity=0
    velocity_change=0
    distance=0
    time=0
    time_change=0
    magnitude=0

    def VectorMagnitude(self,i,j,k=0):
        self.ModifyValues(magnitude=sqrt((i**2)+(j**2)+(k**2)))

    def VelocityAccelerationTime(self, choice):
        self.ModifyValues(velocity_change=self.acceleration*self.TimeChange()) if choice=="velocity" else (self.VelocityChange())/self.acceleration if choice=="time" else (self.VelocityChange())/self.TimeChange() if choice=="acceleration" else "something went wrong"
        if choice=="velocity":
            self.ModifyValues(velocity_change=self.acceleration*self.time)
            self.final_velocity=self.velocity_change
        elif choice=="time":
            self.ModifyValues(time=self.velocity_change*self.acceleration)
        elif choice=="acceleration":
            self.ModifyValues(acceleration=self.velocity_change/self.time)
    def ModifyValues(self,**variables):
        for key, value in variables.items():
            setattr(self, key, value)

    def TimeChange(self):
        self.ModifyValues(time=self.time+self.time_change)
        return self.time

    def VelocityChange(self):
        self.ModifyValues(velocity_change=self.final_velocity-self.initial_velocity)
        return self.velocity_change

    def PrintData(self):
        print(f"""
Force - {self.force}N
Mass - {self.mass}kg
Acceleration - {self.acceleration}m/s^2
Initial Velocity - {self.initial_velocity}m/s
Final Velocity - {self.final_velocity}m/s
Change in velocity - {self.velocity_change}m/s
Distance - {self.distance}m
Time - {self.time}s
Change in time - {self.time_change}s
Magnitude - {self.magnitude}N
            """)

#rect_phy=Physics()
#rect_phy.PrintData()
#rect_phy.ModifyValues(acceleration=9.81,time_change=0.01)
#rect_phy.VelocityAccelerationTime("velocity")
#rect_phy.ModifyValues(acceleration=9.81,time_change=0.01)
#rect_phy.VelocityAccelerationTime("velocity")
#print(rect_phy.velocity_change)
#rect_phy.VectorMagnitude(2,5)
#print(rect_phy.magnitude)