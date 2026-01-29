class GCodeGenerator:
    """Encapsulates G-code generation logic, hiding implementation details from states."""
    
    def __init__(self):
        self._commands = []
        self._initialized = False
    
    def initialize(self, pause_time=0.05):
        """Initialize G-code with setup commands."""
        if not self._initialized:
            self._commands.append("G21 ; Set units to mm")
            self._commands.append("G90 ; Set to absolute positioning")
            self._commands.append("G0 X0 Y0")
            self._commands.append(f"G4 P{pause_time}")
            self._initialized = True
    
    def move_to(self, x, y, pause_time=0.05):
        """Add a move command to the specified coordinates."""
        self._commands.append(f"\n; --- Moving to point ({x}, {y}) ---")
        self._commands.append(f"G0 X{x} Y{y}")
        self._commands.append(f"G4 P{pause_time}")
    
    def pause(self, pause_time=0.05):
        """Add a pause command."""
        self._commands.append(f"G4 P{pause_time}")
    
    def return_home(self):
        """Add commands to return to home position."""
        self._commands.append("\n; --- Job Done, return to home ---")
        self._commands.append("G0 X0 Y0")
    
    def get_commands(self):
        """Get all G-code commands as a list."""
        return self._commands.copy()
    
    def reset(self):
        """Reset the generator, clearing all commands."""
        self._commands = []
        self._initialized = False

