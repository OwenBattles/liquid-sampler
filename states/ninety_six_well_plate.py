from .base_state import State

class NinetySixWellPlate(State): 
    def run(self, context):
        print("UP and Running...")

    def move_to_next_plate(self, context): 
        pass

    def move_to_next_well(self, context):   
        pass

    def pause_over_well(self, context):
        pass