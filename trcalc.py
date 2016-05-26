from trconfig import Configuration
import math
import matplotlib.pyplot as plt


# Baseclass for Trajectory Calculation
# more specific Trajectory Calculators inherit from this class
class TrajectoryCalc:
    
    # startconfig   = Startconfiguration
    # lenght        = distance from front axle to rear axle (m)
    # v1            = velocity at the rear axle (m/s)
    # deltaT        = timeframe between two configurations (s)
    # tM            = timeframe between first and last configuration (s)  
    def __init__(self, startconfig, length, v1, deltaT, tM):
        self.startconfig = startconfig
        self.length = length
        self.v1 = v1
        self.deltaT = deltaT
        self.tM = tM
        self.startconfig.setX0(self.calcX0(self.startconfig))
        self.startconfig.setY0(self.calcY0(self.startconfig))
    
    # Calculate next X1 = X1 + X1_Dot
    def calcX1Next(self, config):
        return config.getX1() + math.cos(config.getTheta1Rad())*(self.v1 * self.deltaT)
    # Calculate next Y1 = Y1 + Y1_Dot
    def calcY1Next(self, config):
        return config.getY1() + math.sin(config.getTheta1Rad())*(self.v1 * self.deltaT)
    # Calculate next Theta = Theta + Theta_Dot
    def calcTheta1Next(self, config):
        return config.getTheta1Rad() + ((math.tan(config.getPhiRad()))/self.length)*(self.v1 * self.deltaT)
        
    # Calculate current X0 from Theta and axle length, X0 = cos(Theta)*L
    # Not really part of the configuration but it is easier to store it to draw
    # the trajectories later
    def calcX0(self,config):
        return config.getX1() + ((math.cos(config.getTheta1Rad()))*self.length)
        
    # Calculate current Y0 from Theta and axle length, Y0 = sin(Theta)*L 
    # Not really part of the configuration but it is easier to store it to draw
    # the trajectories later   
    def calcY0(self,config):
        return config.getY1() + ((math.sin(config.getTheta1Rad()))*self.length)
    
    # Calculate next Phi
    # This is just a placeholder and gets overwritten by the 
    # more specific child Classes
    def calcPhiNext(self,config):
        return 0
    
    # Calculate next Configuration    
    def calcQNext(self, config):
        qNext = Configuration()
        qNext.setX1(self.calcX1Next(config))
        qNext.setY1(self.calcY1Next(config))
        qNext.setTheta1Rad(self.calcTheta1Next(config))
        qNext.setPhiRad(self.calcPhiNext(config))
        qNext.setX0(self.calcX0(config))
        qNext.setY0(self.calcY0(config))
        
        return qNext
        
    # Calculate Trajectory 
    # Represented by a list of configurations
    def calcTrajectory(self):
        trajectory = []
        t = 0
        
        # q is some kind of iterator that keeps the current configuration
        # and is used for the calculation of the next configuration
        q = self.startconfig
        trajectory.append(q)
        
        # we use linear equations here, because of this timedeltas are used 
        # to approximate the path of the car that is in reality a nonlinear 
        # System
        # Calculate new configurations until the end of the main timeframe
        while t <= self.tM:
            
            print(q.toString())
            # the timedelta is added to the already passed time
            t += self.deltaT
            
            # next configuration is calculated based on the current 
            # configuration 
            qNext = self.calcQNext(q)
            
            # set the current point in time 
            # Not really part of the configuration but it is easier to store 
            #it to draw the trajectories later
            qNext.setT(t)
            
            # append the configuration to the trajectory
            trajectory.append(qNext)
            
            # last calculated configuration is now the current configuration
            q = qNext
            
        return trajectory
        
    def plotTrajectory(self):
    
        # trajectory path
        trajectory = self.calcTrajectory()
        
        # lists that store the (x,y) coordinates of the front and rear axle 
        # at any timedelta
        # used for plotting the trajectories
        x1values = []
        y1values = []
        x0values = []
        y0values = []
        
        # iterate over the trajectory (list of configurations) to extract
        # the coordinates of the front and rear axle
        for el in trajectory:
            x1values.append(el.getX1())
            y1values.append(el.getY1())
            x0values.append(el.getX0())
            y0values.append(el.getY0())
        
        # plot trajectory of front axle
        plt.plot(x1values,y1values)
        
        # plot trajectory of rear axle
        plt.plot(x0values,y0values)
        plt.show()
        
        
        
class ConstV2TrCalc(TrajectoryCalc):
     
    def __init__(self, startconfig, length, v1, deltaT, tM, v2):
        TrajectoryCalc.__init__(self,startconfig,length, v1, deltaT, tM)
        self.v2 = v2*3.1415/180
        startconfig.setPhiRad(self.v2)
        
    # overwrite the function for calculating the next phi
    # here steering angle is constant    
    def calcPhiNext(self, config):
        return self.v2
        
class LinearV2TrCalc(TrajectoryCalc):
    
    def __init__(self, startconfig, length, v1, deltaT, tM):
        TrajectoryCalc.__init__(self, startconfig, length, v1, deltaT, tM)
        
    # overwrite the function for calculating the next phi
    # here steering angle changes by a linear function  
    def calcPhiNext(self, config):
        if(config.t <= self.tM/2):
            return ((2*config.t/self.tM)*30)*3.1415/180
        else:
            return (2*(1 - config.t)/self.tM)*30*3.1415/180
            

class TrigonometricV2TrCalc(TrajectoryCalc):
    
    def __init__(self, startconfig, length, v1, deltaT, tM):
        TrajectoryCalc.__init__(self, startconfig, length, v1, deltaT, tM)
    
    # overwrite the function for calculateing the next phi
    # here steering angle changes  a trigeometric function 
    def calcPhiNext(self, config):
        return (30*math.cos((3.1415/self.tM)*config.t))*3.1415/180
            
        

        
        
   
        
            
        
            
        
    
    
        
