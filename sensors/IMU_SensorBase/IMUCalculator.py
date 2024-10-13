import math

class IMUCalculator:
    """
    A class to perform calculations related to IMU (Inertial Measurement Unit) data.
    """

    @staticmethod
    def calculate_angular_velocity_magnitude(gyr_X: float, gyr_Y: float, gyr_Z: float) -> float:
        """
        Calculate the angular velocity magnitude based on gyroscope data.

        Args:
            gyr_X (float): Gyroscope X-axis reading.
            gyr_Y (float): Gyroscope Y-axis reading.
            gyr_Z (float): Gyroscope Z-axis reading.

        Returns:
            float: The angular velocity magnitude.
        """
        return math.sqrt(gyr_X ** 2 + gyr_Y ** 2 + gyr_Z ** 2)