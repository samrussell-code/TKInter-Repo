from math import *
import time as timechecker

class Physics():
    def __init__(self,canvas,parent):
        self.canvas,self.parent=canvas,parent


        self.coords=self.canvas.coords(self.parent)
        self.force=0
        self.mass=0
        self.acceleration=0
        self.initial_velocity=0
        self.final_velocity=0
        self.velocity_change=0
        self.distance=0
        self.start_time=timechecker.time()
        self.initial_time=0
        self.final_time=0
        self.time_change=0
        self.magnitude=0

    def VectorMagnitude(self,i,j,k=0):
        self.ModifyValues(magnitude=sqrt((i**2)+(j**2)+(k**2)))

    def VelocityAccelerationTime(self,choice):
        self.ModifyValues(velocity_change=self.acceleration*self.TimeChange()) if choice=="velocity" else (self.VelocityChange())/self.acceleration if choice=="time" else (self.VelocityChange())/self.TimeChange() if choice=="acceleration" else "something went wrong"
        if choice=="velocity":
            self.initial_velocity=self.final_velocity
            self.ModifyValues(final_velocity=self.acceleration*self.final_time)
            self.velocity_change=(self.final_velocity-self.initial_velocity)/self.time_change       
        elif choice=="time":
            self.ModifyValues(time=self.velocity_change*self.acceleration)
        elif choice=="acceleration":
            self.ModifyValues(acceleration=self.velocity_change/self.final_time)

    def ModifyValues(self,**variables):
        for key, value in variables.items():
            setattr(self, key, value)
            self.coords=self.canvas.coords(self.parent)

    def VelocityDistanceAcceleration(self,choice):
        if choice=="distance":
            self.ModifyValues(distance=(self.final_velocity**2/(2*self.velocity_change)))
            print((self.coords[1])-(self.distance))
    def TimeChange(self):
        self.final_time=timechecker.time()-self.start_time
        self.time_change=self.final_time-self.initial_time
        self.initial_time=self.final_time
        
        return self.time_change

    def VelocityChange(self):
        self.ModifyValues(velocity_change=self.final_velocity-self.initial_velocity)
        return self.velocity_change

    def PrintData(self):
        print(f"""
Coords - {self.coords}
Force - {self.force}N
Mass - {self.mass}kg
Acceleration - {self.acceleration}m/s^2
Initial Velocity - {self.initial_velocity}m/s
Final Velocity - {self.final_velocity}m/s
Change in velocity - {self.velocity_change}m/s
Distance - {self.distance}m
Start Time - {self.start_time}s
Initial Time - {self.initial_time}s
Final Time - {self.final_time}s
Change in time - {self.time_change}s
Magnitude - {self.magnitude}N
            """)

