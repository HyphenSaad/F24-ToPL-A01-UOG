from ..Base.SensorBase import SensorBase
from .OrientationCalculator import OrientationCalculator

class OrientationSensor(SensorBase):
    """
    A class to represent an Orientation Sensor.

    This class inherits from SensorBase and is used to store and process
    orientation sensor data.

    Attributes:
        pitch_X (float): Pitch angle around X-axis.
        roll_Y (float): Roll angle around Y-axis.
        yaw_Z (float): Yaw angle around Z-axis.
        rot_vec_X (float): Rotation vector component along X-axis.
        rot_vec_Y (float): Rotation vector component along Y-axis.
        rot_vec_Z (float): Rotation vector component along Z-axis.

    Inherited Attributes:
        tag (str): Sensor tag or sensor ID to identify sensor type.
        app_timestamp (float): Application timestamp.
        sensor_timestamp (float): Sensor timestamp.
        accuracy (int): Sensor accuracy.

    Methods:
        export_row(index): Export orientation data as a row for CSV file.
    """

    def __init__(self, app_timestamp, sensor_timestamp, pitch_X, roll_Y, yaw_Z, rot_vec_X, rot_vec_Y, rot_vec_Z, accuracy):
        """
        Initialize the OrientationSensor object.

        Args:
            app_timestamp (float): Application timestamp.
            sensor_timestamp (float): Sensor timestamp.
            pitch_X (float): Pitch angle around X-axis.
            roll_Y (float): Roll angle around Y-axis.
            yaw_Z (float): Yaw angle around Z-axis.
            rot_vec_X (float): Rotation vector component along X-axis.
            rot_vec_Y (float): Rotation vector component along Y-axis.
            rot_vec_Z (float): Rotation vector component along Z-axis.
            accuracy (int): Sensor accuracy.
        """
        super().__init__('AHRS', float(app_timestamp), float(sensor_timestamp), int(accuracy))
        self.pitch_X = float(pitch_X)
        self.roll_Y = float(roll_Y)
        self.yaw_Z = float(yaw_Z)
        self.rot_vec_X = float(rot_vec_X)
        self.rot_vec_Y = float(rot_vec_Y)
        self.rot_vec_Z = float(rot_vec_Z)

    def export_row(self, index, include_calculated=False):
        """
        Export orientation data as a row for a CSV file.

        Args:
            index (int): The row index.
            include_calculated (bool): Whether to include calculated values.

        Returns:
            str: A comma-separated string of values representing the row.
        """
        base_row = f'{index},{self.pitch_X},{self.roll_Y},{self.yaw_Z},{self.rot_vec_X},{self.rot_vec_Y},{self.rot_vec_Z}'
        if include_calculated:
            rotation_magnitude = OrientationCalculator.calculate_rotation_magnitude(
                self.rot_vec_X, self.rot_vec_Y, self.rot_vec_Z)
            total_rotation = OrientationCalculator.calculate_total_rotation(
                self.pitch_X, self.roll_Y, self.yaw_Z)
            return f'{base_row},{rotation_magnitude},{total_rotation}'
        return base_row
    
    @staticmethod
    def get_headers(include_calculated=False):
        """
        Get the headers for the CSV file.

        Args:
            include_calculated (bool): Whether to include headers for calculated values.

        Returns:
            str: A comma-separated string of header names.
        """
        return 'index,pitch_x,roll_y,yaw_z,rot_vec_x,rot_vec_y,rot_vec_z' + (',rotation_magnitude,total_rotation' if include_calculated else '')

