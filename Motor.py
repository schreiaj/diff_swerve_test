import math

class Motor:
    """docstring for Motor."""
    def __init__(self, freeSpeedRPM, freeCurrent, stallTorque, stallCurrent, voltage):
        super(Motor, self).__init__()
        self.kFreeSpeed = freeSpeedRPM / 60.0 * 2.0 * math.pi
        self.kFreeCurrent = freeCurrent
        self.kStallCurrent = stallCurrent
        self.kStallTorque = stallTorque
        self.kVoltageSpec = voltage
        # V = IR + W/k_v
        # At stall:
        #  V = stallCurrent/R
        #  R = V/stallCurrent
        self.k_r = self.kVoltageSpec/self.kStallCurrent
        # At free speed:
        #  V = freeCurrent * R + freeSpeed/k_v
        #  V - (freeCurrent * R) = freeSpeed/k_v
        #  K_v(V - (freeCurrent * R)) = FreeSpeed
        #  K_v = freeSpeed/ (V - (freeCurrent * R))
        self.k_v = self.kFreeSpeed / (self.kVoltageSpec - self.kFreeCurrent * self.k_r)
        # t = I * k_t
        # t/I = k_t
        self.k_t = self.kStallTorque / self.kStallCurrent

    def torqueAtRPM(self, voltage, rpm):
        _w = rpm / 60.0 * 2.0 * math.pi
        _voltage = abs(voltage)
        sign = voltage/max(_voltage, 1)
        return sign*min(((_voltage - _w/self.k_v)/self.k_r) * self.k_t, self.kStallTorque)
