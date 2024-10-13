from ..Base.SensorBase import SensorBase
from .GyroscopeCalculator import GyroscopeCalculator

class GyroscopeSensor(SensorBase):
    """
    A class to represent a Gyroscope Sensor.

    This class inherits from SensorBase and is used to store and process
    gyroscope sensor data.

    Attributes:
        gyr_X (float): Angular velocity around the X-axis.
        gyr_Y (float): Angular velocity around the Y-axis.
        gyr_Z (float): Angular velocity around the Z-axis.

    Inherited Attributes:
        tag (str): Sensor tag or sensor ID to identify sensor type.
        app_timestamp (float): Application timestamp.
        sensor_timestamp (float): Sensor timestamp.
        accuracy (int): Sensor accuracy.

    Methods:
        export_row(index, include_calculated): Export gyroscope data as a row for CSV file.
        get_headers(include_calculated): Get the headers for the CSV file.
    """

    def __init__(self, app_timestamp, sensor_timestamp, gyr_X, gyr_Y, gyr_Z, accuracy):
        """
        Initialize the GyroscopeSensor object.

        Args:
            app_timestamp (float): Application timestamp.
            sensor_timestamp (float): Sensor timestamp.
            gyr_X (float): Angular velocity around the X-axis.
            gyr_Y (float): Angular velocity around the Y-axis.
            gyr_Z (float): Angular velocity around the Z-axis.
            accuracy (int): Sensor accuracy.
        """
        super().__init__('GYRO', float(app_timestamp), float(sensor_timestamp), int(accuracy))
        self.gyr_X = float(gyr_X)
        self.gyr_Y = float(gyr_Y)
        self.gyr_Z = float(gyr_Z)

    def export_row(self, index, include_calculated=False):
        """
        Export gyroscope data as a row for a CSV file.

        Args:
            index (int): The row index.
            include_calculated (bool): Whether to include calculated values.

        Returns:
            str: A comma-separated string of values representing the row.
        """
        base_row = f'{index},{self.gyr_X},{self.gyr_Y},{self.gyr_Z}'
        if include_calculated:
            angular_velocity = GyroscopeCalculator.calculate_angular_velocity(self.gyr_X, self.gyr_Y, self.gyr_Z)
            return f'{base_row},{angular_velocity}'
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
        return 'index,gyr_x,gyr_y,gyr_z' + (',angular_velocity_magnitude' if include_calculated else '')