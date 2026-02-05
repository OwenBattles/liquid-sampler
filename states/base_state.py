from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def run(self, context):
        """This function runs the entire protocol"""
        pass

    @abstractmethod
    def move_to_next_plate(self, context): 
        """This function handles the moving from one plate to another"""   
        pass

    @abstractmethod
    def move_to_next_well(self, context):
        """Move from one well to another within a plate."""
        pass

    @abstractmethod
    def move_to_next_row(self, context):
        """Move from one row to another within a plate."""
        pass
