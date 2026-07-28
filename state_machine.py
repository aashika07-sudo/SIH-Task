"""
Water Point State Machine

States:
NORMAL
DISTURBANCE
RECOVERY
STABLE
"""


class WaterPointStateMachine:

    NORMAL = "NORMAL"
    DISTURBANCE = "DISTURBANCE"
    RECOVERY = "RECOVERY"
    STABLE = "STABLE"

    def __init__(
        self,
        target=100
    ):
        self.target = target
        self.state = self.NORMAL

    def update(
        self,
        actual_value,
        disturbance=False
    ):
        """
        Updates the current state of the water point.
        """

        if disturbance:
            self.state = self.DISTURBANCE

        elif actual_value < self.target - 5:
            self.state = self.RECOVERY

        else:
            self.state = self.STABLE

        return self.state

    def get_state(self):
        return self.state