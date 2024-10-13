import numpy as np

class AccelerometerCalculator:
    """
    A class to perform calculations related to accelerometer data.
    """

    @staticmethod
    def calculate_average_acceleration(acc_X: float, acc_Y: float, acc_Z: float) -> float:
        """
        Calculate the average acceleration across all axes.

        Args:
            acc_X (float): Acceleration along the X-axis.
            acc_Y (float): Acceleration along the Y-axis.
            acc_Z (float): Acceleration along the Z-axis.

        Returns:
            float: The average acceleration.
        """
        return (acc_X + acc_Y + acc_Z) / 3

    @staticmethod
    def calculate_magnitude(acc_X: float, acc_Y: float, acc_Z: float) -> float:
        """
        Calculate the magnitude of acceleration across all axes.

        Args:
            acc_X (float): Acceleration along the X-axis.
            acc_Y (float): Acceleration along the Y-axis.
            acc_Z (float): Acceleration along the Z-axis.

        Returns:
            float: The magnitude of acceleration.
        """
        return np.sqrt(acc_X**2 + acc_Y**2 + acc_Z**2)