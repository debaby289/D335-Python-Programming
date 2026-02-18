class LooseChange:
    def __init__(self, value):
        self.value = value  
        
    def __add__(self, other):
        new_value = self.value + other.value
        return LooseChange(new_value)
                                     