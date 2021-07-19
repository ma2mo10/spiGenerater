import spiGenerater as sg

class spiParams:
    def __init__(self, vt=0.6, sigma=0, y=1):
        self.vt = vt
        self.sigma = sigma
        self.y = y

    def getparms(self):
        return self.vt, self.sigma, self.y

    
        

