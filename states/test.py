from .base_state import State


class TestProtocol(State):
    """Simple test protocol for validating the system."""
    
    def run(self, context):
        """Execute a simple test protocol that moves to a few test positions."""
        # Get services from context (information hiding - we don't know how they work)
        gcode = context.gcode_generator
        file_writer = context.file_writer
        
        # Protocol configuration
        test_positions = [
            (0.0, 0.0),
            (50.0, 25.0),
            (100.0, 50.0),
            (50.0, 75.0),
            (0.0, 0.0)  # Return home
        ]
        pause_time = 0.1  # seconds
        
        # Initialize G-code
        gcode.initialize(pause_time=pause_time)
        
        # Execute protocol: move to each test position
        for x, y in test_positions:
            gcode.move_to(x, y, pause_time=pause_time)
        
        # Return home (if not already there)
        if test_positions[-1] != (0.0, 0.0):
            gcode.return_home()
        
        # Write G-code to file
        filename = "test_protocol.nc"
        gcode_commands = gcode.get_commands()
        
        if file_writer.write_gcode_to_file(gcode_commands, filename):
            print(f"Success! Test protocol written to '{filename}'")
        else:
            print("Error: Failed to write test protocol file")
    
    def move_to_next_plate(self, context):
        """Move to the next plate in the protocol."""
        pass
    
    def move_to_next_well(self, context):
        """Move to the next well in the current plate."""
        pass

    def move_to_next_row(self, context):
        """Move to the next row in the current plate."""
        pass

    def pause_over_well(self, context):
        """Pause over the current well."""
        pass

