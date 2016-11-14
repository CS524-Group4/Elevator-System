
class Door_sensor:
    def _init_(self):
        self.object = False;

    def There_is_object (self):
        if self.object == False:
            return False
        else:
            return True


