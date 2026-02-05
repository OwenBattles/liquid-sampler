from .base_state import State
from services.constants import WELL_DIAMETER


class BasicCulturing(State):
    """Basic culturing state for the robot."""

    def __init__(self, pause_time=0.15):
        self.pause_time = pause_time
        self.x_position = 0.0
        self.y_position = 0.0
        self.well_diameter = WELL_DIAMETER

    def run(self, context):
        """Execute a basic culturing protocol."""
        gcode = context.gcode_generator
        file_writer = context.file_writer

        gcode.initialize(pause_time=self.pause_time)

        for i in range(12):
            for _ in range(7):
                self.move_to_next_well(context)
            if i != 11: self.move_to_next_row(context)

        filename = "basic_culturing.nc"
        if file_writer.write_gcode_to_file(gcode.get_commands(), filename):
            print(f"Success! Basic culturing protocol written to '{filename}'")
        else:
            print("Error: Failed to write basic culturing protocol file")

    def move_to_next_plate(self, context):
        """Move to the next plate in the protocol."""
        pass

    def move_to_next_well(self, context):
        context.gcode_generator.move_to(
            self.x_position,
            self.y_position + self.well_diameter,
            pause_time=self.pause_time,
        )
        self.y_position += self.well_diameter

    def move_to_next_row(self, context):
        context.gcode_generator.move_to(
            self.x_position + self.well_diameter,
            0.0, pause_time=self.pause_time,
        )
        self.x_position += self.well_diameter
        self.y_position = 0.0

