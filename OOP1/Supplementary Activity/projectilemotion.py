import math

def projectilemotion_solver(angle, speed):
    g = 9.8
    theta = math.radians(angle)
    r = ((speed**2) * math.sin(2*theta)) / g
    h = ((speed**2) * math.sin(2*theta)) / (2 * g)
    return r, h



