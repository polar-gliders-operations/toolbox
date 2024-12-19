import numpy as np

def calculate_distance(horz_speed_gsm, delta_t):
    """
    Calculate the cumdistance relative to the current based on horizontal speed of the GSM model and delta_t.

    Parameters:
    horz_speed_gsm (np.ndarray): Array of horizontal speeds (in m/s).
    delta_t (np.ndarray): Time step(s) in seconds. Array of the same length as horz_speed_gsm.

    Returns:
    np.ndarray: Cumulative distance in meters.
    """
    # Replace NaN values in horz_speed_gsm with 0
    horz_speed = np.nan_to_num(horz_speed_gsm)

    # Ensure horz_speed is a copy to avoid modifying the original input
    horz_speed = horz_speed.copy()

    # Set the first value of horz_speed to 0
    horz_speed[0] = 0

    # Update subsequent values to the average of the current and previous value
    for i in range(1, len(horz_speed)):
        horz_speed[i] = (horz_speed[i] + horz_speed[i - 1]) / 2

    # Calculate delta_distance and cumulative distance
    delta_distance = horz_speed * delta_t
    distance = np.cumsum(delta_distance)

    return distance