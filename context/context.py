from services.gcode_generator import GCodeGenerator
from services.file_writer import FileWriter


class DeviceContext:
    """Context that provides services to states and manages state transitions."""
    
    def __init__(self, initial_state):
        self._state = initial_state
        self._gcode_generator = GCodeGenerator()
        self._file_writer = FileWriter()

    def transition_to(self, state):
        print(f"Transitioning: {self._state} -> {state}")
        self._state = state

    def run(self):
        self._state.run(self)
    
    @property
    def gcode_generator(self):
        """Get the G-code generator service."""
        return self._gcode_generator
    
    @property
    def file_writer(self):
        """Get the file writer service."""
        return self._file_writer