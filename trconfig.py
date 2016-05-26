import math

class Configuration:

    def __init__(self):
        #[x1,y1,theta1,phi]
        self.x1 = 0
        self.y1 = 0
        self.theta1 = 0
        self.phi = 0
        self.x0 = 0
        self.y0 = 0
        self.t = 0
        
    def setX1(self,x1):
        self.x1 = x1
        
    def getX1(self):
        return self.x1
        
    def setY1(self,y1):
        self.y1 = y1
        
    def getY1(self):
        return self.y1
        
    def setTheta1Deg(self,theta1):
        self.theta1 = (theta1*3.1415)/180
        
    def setTheta1Rad(self,theta1):
        self.theta1 = theta1
        
    def getTheta1Deg(self):
        return self.theta1*180/3.1415
        
    def getTheta1Rad(self):
        return self.theta1
        
    def setPhiDeg(self,phi):
        self.phi = phi*3.1415/180
    
    def setPhiRad(self,phi):
        self.phi = phi
        
    def getPhiDeg(self):
        return self.phi*180/3.1415
    
    def getPhiRad(self):
        return self.phi
    
    def setX0(self,x0):
        self.x0 = x0
    
    def getX0(self):
        return self.x0
        
    def setY0(self,y0):
        self.y0 = y0
        
    def getY0(self):
        return self.y0
    
    def setT(self,t):
        self.t = t
    
    def getT(self):
        return t 
        
    def toString(self):
        st = "["
        st += str(self.x1)
        st += ", "
        st += str(self.y1)
        st += ", "
        st += str(self.theta1)
        st += "PI, "
        st += str(self.phi)
        st += "PI, "
        st += str(self.x0)
        st += ", "
        st += str(self.y0)
        st += ", "
        st += str(self.t)
        st += "]"
        
        return st
    
   
