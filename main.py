from context.context import DeviceContext
from states.basic_culturing import BasicCulturing

if __name__ == "__main__":
    context = DeviceContext(BasicCulturing())
    context.run()