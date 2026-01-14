from context.context import DeviceContext
from states.ninety_six_well_plate import NinetySixWellPlate

if __name__ == "__main__":
    context = DeviceContext(NinetySixWellPlate())

    context.run()