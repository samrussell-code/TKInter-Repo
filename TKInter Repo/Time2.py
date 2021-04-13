from datetime import datetime
import pickle, os
class Time2():
    def __init__(self):
        debug_mode=False;self.debug_mode=debug_mode
        if os.path.isfile("times.txt"):
            with open("times.txt", "rb")as file:
                self.savedTimes=pickle.loads(file.read())
        else:
            savedTimes=[]
            self.savedTimes=savedTimes

    def CompareTime(self,time): #compares the 2 stored values of time and returns the total time change in seconds
        yearDiff=time[1][0]-time[0][0] #difference between saved year and current year
        dayDiff=time[1][1]-time[0][1] #difference between saved day and current day
        secondDiff=time[1][2]-time[0][2] #difference between saved second and current second
        dayDiff=dayDiff+365*yearDiff if yearDiff>0 else dayDiff
        secondDiff=secondDiff+86400*dayDiff if dayDiff>0 else secondDiff
        
        return secondDiff
    
    def GetTime(self,type="null"):
        new=datetime.now()
        year,day,second=new.strftime("%Y"),new.strftime("%j"),new.strftime("%H%M%S")
        year,day,second=int(year),int(day),int(second)
        if type!="counting":
            time=self.StoreTime(year,day,second)
            return time
        else:
            return year,day,second

    def StoreTime(self,year,day,second): #stores the two most recent calls, so the time between them can be compared.
        if os.path.isfile("times.txt"):
            with open("times.txt", "rb")as file:
                self.savedTimes=pickle.loads(file.read())
        savedPos=len(self.savedTimes)
        self.savedTimes=[self.savedTimes[1]] if savedPos > 1 else self.savedTimes
        self.savedTimes.insert(savedPos, [year,day,second])
        with open("times.txt", "wb") as file:
            pickle.dump(self.savedTimes, file)
        return self.savedTimes

    def emptyProc(): #count time is time.sleep but can actively do processes in the background. If no method is called, this one is chosen.
        return

    def CountTime(self,duration,procedure=emptyProc): #A counter like time.sleep but built myself inside of Time2 so time is now void! :)
        initTime=self.GetTime(type="counting") #stores initial time where counting begins
        if self.debug_mode==True: print(duration,"Seconds starting...") 
        currentTime=0 #starting time will always be at 0
        while currentTime<duration:
            newTime=self.GetTime(type="counting") #grabs the time again but is rerouted by the special arg 'counting' so it returns tuple instead of list
            list=self.StoreTime(initTime[0],initTime[1],initTime[2])
            list=self.StoreTime(newTime[0],newTime[1],newTime[2])
            currentTime=self.CompareTime(list)

            result=procedure()
           
        if self.debug_mode==True: print(duration,"Seconds have passed.")
        return result



#timemachine=Time2()
#time=timemachine.GetTime()
#print(timemachine.CompareTime(time))
#timemachine.debug_mode=True
#timemachine.CountTime(5)