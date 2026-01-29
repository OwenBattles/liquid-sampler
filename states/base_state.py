from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def run(self, context):
        """This function orchestrates the entire process"""
        pass

    @abstractmethod
    def move_to_next_plate(self, context): 
        """This function handles the moving from one plate to another"""   
        pass

    @abstractmethod
    def move_to_next_well(self, context):   
        """This function handles the moving from one well to another within a plate"""    
        pass

    def pause_over_well(self, context):
        """This function handles how long the syringe hovers over each well"""
        pass
