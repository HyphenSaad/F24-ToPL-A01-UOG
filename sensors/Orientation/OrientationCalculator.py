import math

class OrientationCalculator:
    """
    A class to perform calculations related to orientation sensor data.
    """

    @staticmethod
    def calculate_rotation_magnitude(rot_vec_X, rot_vec_Y, rot_vec_Z):
        """
        Calculate the magnitude of the rotation vector.

        Args:
            rot_vec_X (float): Rotation vector component along X-axis.
            rot_vec_Y (float): Rotation vector component along Y-axis.
            rot_vec_Z (float): Rotation vector component along Z-axis.

        Returns:
            float: The magnitude of the rotation vector.
        """
        return math.sqrt(rot_vec_X ** 2 + rot_vec_Y ** 2 + rot_vec_Z ** 2)
    
    @staticmethod
    def calculate_total_rotation(pitch_X, roll_Y, yaw_Z):
        """
        Calculate the total rotation by summing the absolute values of pitch, roll, and yaw.

        Args:
            pitch_X (float): Pitch angle around X-axis.
            roll_Y (float): Roll angle around Y-axis.
            yaw_Z (float): Yaw angle around Z-axis.

        Returns:
            float: The total rotation.
        """
        return abs(pitch_X) + abs(roll_Y) + abs(yaw_Z)