
class position_sensor:
    def _init_(self):
        self.Difference_In_Position = 0.5; # 0.5 centimeter

    def is_Parallel (self):
        if self.Difference_In_Position <= 0.5:
            return True
        else:
            return False


