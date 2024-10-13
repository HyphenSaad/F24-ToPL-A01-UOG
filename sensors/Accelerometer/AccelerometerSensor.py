from ..Base.SensorBase import SensorBase
from .AccelerometerCalculator import AccelerometerCalculator

class AccelerometerSensor(SensorBase):
    """
    A class to represent an Accelerometer Sensor.

    This class inherits from SensorBase and is used to store and process
    accelerometer sensor data.

    Attributes:
        acc_X (float): Acceleration along the X-axis.
        acc_Y (float): Acceleration along the Y-axis.
        acc_Z (float): Acceleration along the Z-axis.

    Inherited Attributes:
        tag (str): Sensor tag or sensor ID to identify sensor type.
        app_timestamp (float): Application timestamp.
        sensor_timestamp (float): Sensor timestamp.
        accuracy (int): Sensor accuracy.

    Methods:
        export_row(index): Export accelerometer data as a row for CSV file.
    """

    def __init__(self, app_timestamp, sensor_timestamp, acc_X, acc_Y, acc_Z, accuracy):
        """
        Initialize the AccelerometerSensor object.

        Args:
            app_timestamp (float): Application timestamp.
            sensor_timestamp (float): Sensor timestamp.
            acc_X (float): Acceleration along the X-axis.
            acc_Y (float): Acceleration along the Y-axis.
            acc_Z (float): Acceleration along the Z-axis.
            accuracy (int): Sensor accuracy.
        """
        super().__init__('ACCE', float(app_timestamp), float(sensor_timestamp), int(accuracy))
        self.acc_X = float(acc_X)
        self.acc_Y = float(acc_Y)
        self.acc_Z = float(acc_Z)

    def export_row(self, index, include_calculated=False):
        """
        Export accelerometer data as a row for a CSV file.

        Args:
            index (int): The row index.
            include_calculated (bool): Whether to include calculated values.

        Returns:
            str: A comma-separated string of values representing the row.
        """
        base_row = f'{index},{self.acc_X},{self.acc_Y},{self.acc_Z}'
        if include_calculated:
            avg_acc = AccelerometerCalculator.calculate_average_acceleration(self.acc_X, self.acc_Y, self.acc_Z)
            magnitude = AccelerometerCalculator.calculate_magnitude(self.acc_X, self.acc_Y, self.acc_Z)
            return f'{base_row},{avg_acc},{magnitude}'
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
        return 'index,acc_x,acc_y,acc_z' + (',avg_acc,magnitude' if include_calculated else '')