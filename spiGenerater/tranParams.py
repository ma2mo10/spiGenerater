import spiGenerater as sg

class tranParams:
    def __init__(self, vt=0.6, sigma=0, seed=1, mos='p'):
        self.vt = vt
        self.sigma = sigma
        self.seed = seed
        self.mos = mos

    def getparms(self):
        return self.vt, self.sigma, self.seed, self.mos

    
        

