# pid_control.py

class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_error = 0
        self.integral = 0

    def compute(self, setpoint, measured_value):
        """
        Compute the control signal using PID control.
        """
        error = setpoint - measured_value
        self.integral += error
        derivative = error - self.prev_error
        output = (self.kp * error) + (self.ki * self.integral) + (self.kd * derivative)
        self.prev_error = error
        return output

if __name__ == "__main__":
    pid = PIDController(1.0, 0.1, 0.05)
    control_signal = pid.compute(10, 8)
    print("Control Signal:", control_signal)
