import numpy as np

class GyroscopeCalculator:
    """
    A class to perform calculations related to gyroscope data.
    """

    @staticmethod
    def calculate_angular_velocity(gyr_X: float, gyr_Y: float, gyr_Z: float) -> float:
        """
        Calculate the angular velocity magnitude.

        Args:
            gyr_X (float): Angular velocity around the X-axis.
            gyr_Y (float): Angular velocity around the Y-axis.
            gyr_Z (float): Angular velocity around the Z-axis.

        Returns:
            float: The angular velocity magnitude.
        """
        return np.sqrt(gyr_X**2 + gyr_Y**2 + gyr_Z**2)

    @staticmethod
    def calculate_rotation_angle(angular_velocity: float, time_delta: float) -> float:
        """
        Calculate the rotation angle.

        Args:
            angular_velocity (float): The angular velocity magnitude.
            time_delta (float): The time difference between measurements.

        Returns:
            float: The calculated rotation angle.
        """
        return angular_velocity * time_delta