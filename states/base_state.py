from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def run(ABC):
        """This function orchestrates the entire process"""

    @abstractmethod
    def move_to_next_plate(ABC): 
        """This function handles the moving from one plate to another"""   
        pass

    @abstractmethod
    def move_to_next_well(ABC):   
        """This function handles the moving from one well to another within a plate"""    
        pass

    def pause_over_well(ABC):
        """This function handles how long the syringe hovers over each well"""

    