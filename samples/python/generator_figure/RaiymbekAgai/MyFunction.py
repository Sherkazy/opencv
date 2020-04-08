import numpy as np
def radian(angle):
    return angle*np.pi/180.0

def PolarRandom1(m,n,angle0,angle1,radius0, radius1):
    if radius0 < np.amin([m,n])/2.0 and radius1 < np.amin([m,n])/2.0:
        radius = np.random.randint(low = radius0, high = radius1, size = 1)    
        angle = np.random.randint(low = angle0, high = angle1, size = 1)    
        x = int(n/2.0+radius*np.cos(radian(angle)))
        y = int(m/2.0+radius*np.sin(radian(angle)))
    if x < 0 or x > n or y < 0 or y > m:
        print("Ошибка")
    return x,y
