import math

class MagnetometerCalculator:
    """
    A class to perform calculations related to magnetometer data.
    """

    @staticmethod
    def calculate_magnitude(mag_x: float, mag_y: float, mag_z: float) -> float:
        """
        Calculate the magnitude of the magnetic field.

        Args:
            mag_x (float): Magnetometer reading on X-axis.
            mag_y (float): Magnetometer reading on Y-axis.
            mag_z (float): Magnetometer reading on Z-axis.

        Returns:
            float: The magnitude of the magnetic field.
        """
        return math.sqrt(mag_x**2 + mag_y**2 + mag_z**2)

    @staticmethod
    def calculate_compass_heading(mag_x: float, mag_y: float) -> float:
        """
        Calculate the compass heading based on magnetometer readings.

        Args:
            mag_x (float): Magnetometer reading on X-axis.
            mag_y (float): Magnetometer reading on Y-axis.

        Returns:
            float: The compass heading in degrees (0-360).
        """
        heading = math.atan2(mag_y, mag_x)
        heading = math.degrees(heading)
        if heading < 0:
            heading += 360
        return heading