import numpy as np
import matplotlib.pyplot as plt

class membership:
    
    def __init__(self, *args, **kwargs):
        try:
            self.x = np.linspace(args[0], args[1], args[2])
            self.y = np.zeros_like(self.x)
        except:
            self.x = np.array([kwargs.get('x_input')]).astype('float')
            self.y = np.zeros_like(self.x)
    
    def increasing(self, a, b):
        for i in range(len(self.x)):
            if self.x[i] <= a:
                self.y[i] = 0
            elif self.x[i] >= b:
                self.y[i] = 1
            else:
                self.y[i] = (self.x[i]-a)/(b-a)
        return self
    
    def decreasing(self, a, b):
        self.y = 1-self.increasing(a, b).y
        return self
    
    def trapezoid(self, a, b, c, d):
        for i in range(len(self.x)):
            if self.x[i] < a:
                self.y[i] = 0
            elif self.x[i] > d:
                self.y[i] = 0    
            elif self.x[i] >= a and self.x[i] <= b:
                self.y[i] = (self.x[i]-a)/(b-a)
            elif self.x[i] >= b and self.x[i] <= c:
                self.y[i] = 1
            elif self.x[i] >= c and self.x[i] <= d:
                self.y[i] = (d-self.x[i])/(d-c)
        return self
    
    def gaussian(self, mu, sig):
        self.y = np.exp(-(self.x-mu)**2/(2*sig**2))
        return self
    
    def sigmoid(self, a, b):
        self.y = 1/(1+np.exp(-a*(self.x-b)))
        return self

mem_inc = membership(0, 20, 101).increasing(5, 15)
mem_dec = membership(0, 20, 101).decreasing(5, 15)

inp_mem_inc = membership(x_input=12).increasing(5, 15)
inp_mem_dec = membership(x_input=12).decreasing(5, 15)

plt.plot(mem_inc.x, mem_inc.y);
plt.plot(mem_dec.x, mem_dec.y);
plt.scatter(inp_mem_inc.x, inp_mem_inc.y);
plt.scatter(inp_mem_dec.x, inp_mem_dec.y);