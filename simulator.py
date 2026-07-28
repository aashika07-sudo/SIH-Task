"""
Village Water Point Monitoring
Simulation Module

This module simulates:
1. Normal water point operation
2. A sudden step disturbance
3. Controller response
4. Recovery toward the target value
"""


def run_step_disturbance_simulation(
    target=100,
    initial_value=100,
    disturbance_time=10,
    disturbance_amount=40,
    recovery_rate=0.20,
    total_time=40
):
    """
    Simulates a water point system with a step disturbance.

    Parameters:
        target: Desired water availability percentage.
        initial_value: Initial water availability percentage.
        disturbance_time: Time at which disturbance occurs.
        disturbance_amount: Sudden decrease caused by disturbance.
        recovery_rate: Controller recovery rate.
        total_time: Total simulation time.

    Returns:
        Dictionary containing simulation results.
    """

    time_values = []
    target_values = []
    actual_values = []
    disturbance_values = []
    controller_values = []

    actual_value = initial_value

    for time in range(total_time + 1):

        # Target remains constant
        target_value = target

        # Step disturbance
        if time == disturbance_time:
            actual_value = max(
                0,
                actual_value - disturbance_amount
            )

        # Calculate error
        error = target_value - actual_value

        # Controller action
        controller_action = recovery_rate * error

        # Apply controller
        if time > disturbance_time:
            actual_value = actual_value + controller_action

        # Keep value between 0 and 100
        actual_value = max(
            0,
            min(100, actual_value)
        )

        # Store values
        time_values.append(time)
        target_values.append(target_value)
        actual_values.append(round(actual_value, 2))

        if time >= disturbance_time:
            disturbance_values.append(
                disturbance_amount
            )
        else:
            disturbance_values.append(0)

        controller_values.append(
            round(controller_action, 2)
        )

    final_value = actual_values[-1]

    recovered = abs(
        target - final_value
    ) <= 5

    return {
        "time": time_values,
        "target": target_values,
        "actual": actual_values,
        "disturbance": disturbance_values,
        "controller": controller_values,
        "final_value": final_value,
        "recovered": recovered
    }


def calculate_uptime_percentage(
    working_points,
    total_points
):
    """
    Calculates the overall uptime percentage.
    """

    if total_points == 0:
        return 0

    uptime = (
        working_points /
        total_points
    ) * 100

    return round(uptime, 2)