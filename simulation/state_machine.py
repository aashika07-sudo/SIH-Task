"""
Simulation State Machine

This file handles the states used
during the step disturbance simulation.
"""


class SimulationStateMachine:

    NORMAL = "NORMAL"
    DISTURBANCE = "DISTURBANCE"
    RECOVERY = "RECOVERY"
    STABLE = "STABLE"

    def __init__(
        self,
        target=100
    ):
        self.target = target
        self.current_state = self.NORMAL

    def process(
        self,
        actual_value,
        disturbance=False
    ):
        if disturbance:
            self.current_state = self.DISTURBANCE

        elif actual_value < self.target - 5:
            self.current_state = self.RECOVERY

        else:
            self.current_state = self.STABLE

        return self.current_state

    def get_state(self):
        return self.current_state