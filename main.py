from context.context import DeviceContext
from states.test import TestProtocol

if __name__ == "__main__":
    context = DeviceContext(TestProtocol())
    context.run()