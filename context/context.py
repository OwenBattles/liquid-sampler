class DeviceContext:
    def __init__(self, initial_state):
        self._state = initial_state

    def transition_to(self, state):
        print(f"Transitioning: {self._state} -> {state}")
        self._state = state

    def run(self):
        self._state.run(self)