class DiffSwerveController:
    def __init__(self):
        super(DiffSwerveController, self).__init__()
        self.k_p_angle = 1.0
        self.k_d_angle = 0
        self.k_p_rpm = 1.0
        self.k_d_rpm = 0

    def step(self, targetAngle, targetRPM, currentAngle, currentRPM):
        angleError = targetAngle - currentAngle
        speedError = targetRPM - currentRPM
        out = self.k_p_angle * angleError
        return (out + speedError * self.k_p_rpm, out - speedError * self.k_p_rpm)


from DiffSwerve import DiffSwerve
import Helper
controller = DiffSwerveController()
sim = DiffSwerve()
for i in range(0, 1000):
    (a,b) = controller.step(45, 150, sim.steer_angle, Helper.RadsToRPM(sim.drive_w))
    sim.step(a,b,.001)
    print(i*.01, sim.steer_angle, Helper.RadsToRPM(sim.drive_w))
