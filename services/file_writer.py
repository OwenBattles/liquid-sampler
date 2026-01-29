class FileWriter:
    """Encapsulates file I/O operations, hiding filesystem details from states."""
    
    def write_gcode_to_file(self, gcode_commands, filename):
        """Write G-code commands to a file."""
        try:
            with open(filename, "w") as f:
                for line in gcode_commands:
                    f.write(line + "\n")
            return True
        except IOError as e:
            print(f"Error writing file '{filename}': {e}")
            return False

