import math

def RPMToRads(rpm):
    return rpm/ 60.0 * 2.0 * math.pi

def RadsToRPM(rads):
    return rads * 60.0 / 2.0 / math.pi
