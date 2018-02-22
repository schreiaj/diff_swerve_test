from Motor import Motor
import Helper

class DiffSwerve:
    """docstring for DiffSwerve"""
    def __init__(self):
        super(DiffSwerve, self).__init__()
        # I don't see ever wanting different reductions
        self.reductionA = 1/10.0
        self.reductionB = 1/10.0
        self.motorA = Motor(18730, 0.7, .71, 134, 12.0)
        self.motorB = Motor(18730, 0.7, .71, 134, 12.0)
        self.driveReduction = 4/1.0
        self.k_steer_i = 4.0
        self.k_drive_i = 1.0
        self.steer_angle = 0
        self.motorA_w = 0
        self.motorB_w = 0
        self.steer_w = 0
        self.drive_w = 0
    def step(self, vA, vB, dt):
        torqueA = self.motorA.torqueAtRPM(vA, Helper.RadsToRPM(self.motorA_w*self.reductionA)) / self.reductionA
        torqueB = self.motorB.torqueAtRPM(vB, Helper.RadsToRPM(self.motorB_w*self.reductionB)) / self.reductionB
        self.motorA_w = torqueA / (self.k_steer_i + self.k_drive_i) * dt
        self.motorB_w = torqueB / (self.k_steer_i + self.k_drive_i) * dt
        self.steer_w += (torqueA + torqueB) / self.k_steer_i * dt
        self.drive_w += ((torqueA - torqueB) / self.k_drive_i  * dt) * self.driveReduction
        self.steer_angle += self.steer_w *dt
