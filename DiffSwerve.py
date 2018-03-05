from Motor import Motor
import Helper
import math

class DiffSwerve:
    """docstring for DiffSwerve"""
    def __init__(self):
        super(DiffSwerve, self).__init__()
        # I don't see ever wanting different reductions
        self.reductionA = 1/10.0
        self.reductionB = 1/10.0
        self.motorA = Motor(18730, 0.7, .71, 134, 12.0)
        self.motorB = Motor(18730, 0.7, .71, 134, 12.0)
        self.r_ab = 3.5
        self.r_d = .75
        self.w_a = 0.0
        self.w_b = 0.0
        self.w_w = 0.0 # wheel omega
        self.angle =0
        self.wheel_diameter = 2.5
        self.k_steer_i = .47
        self.k_drive_i = .05
        self.v = 0
        self.v_ad = 0
        self.v_bd = 0


    def step(self, vA, vB, dt):
        t_a = self.motorA.torqueAtRPM(vA, self.w_a * self.reductionA) / self.reductionA
        t_b = self.motorB.torqueAtRPM(vB, self.w_b * self.reductionB) / self.reductionB
        self.w_a = (t_a/self.k_steer_i) * dt
        self.w_b = (t_b/self.k_steer_i) * dt
        self.v_ad = self.v_ad + self.w_a * 2 * math.pi * self.r_ab
        self.v_bd = self.v_bd + self.w_b * 2 * math.pi * self.r_ab
        v_z = (self.v_ad + self.v_bd)/2
        w_z = v_z / (2*math.pi * (self.r_ab))
        self.angle = w_z * dt + self.angle
        self.w_w = ((self.v_ad - self.v_bd)/2)/(2*math.pi*self.r_d)
        self.v = self.w_w * math.pi * self.wheel_diameter


        # torqueA = self.motorA.torqueAtRPM(vA, Helper.RadsToRPM(self.motorA_w*self.reductionA)) / self.reductionA
        # torqueB = self.motorB.torqueAtRPM(vB, Helper.RadsToRPM(self.motorB_w*self.reductionB)) / self.reductionB
        # self.motorA_w = torqueA / (self.k_steer_i + self.k_drive_i) * dt
        # self.motorB_w = torqueB / (self.k_steer_i + self.k_drive_i) * dt
        # self.steer_w += (torqueA + torqueB) / self.k_steer_i * dt
        # self.drive_w += ((torqueA - torqueB) / self.k_drive_i  * dt) * self.driveReduction
        # self.steer_angle += self.steer_w *dt
