from abc import ABC, abstractmethod

class SensorBase(ABC):
    """
    An abstract base class to store common attributes and methods for all sensors.

    This class serves as a foundation for various sensor types, providing a
    consistent interface and shared functionality.

    Attributes:
        tag (str): Sensor tag or sensor ID to identify the sensor type.
        app_timestamp (float, optional): Application timestamp.
        sensor_timestamp (float, optional): Sensor timestamp.
        accuracy (int, optional): Sensor accuracy.

    Methods:
        export_row(index): Abstract method to export sensor data as a row for a CSV file.
    """

    def __init__(self, tag, app_timestamp=None, sensor_timestamp=None, accuracy=None):
        """
        Initialize the SensorBase object.

        Args:
            tag (str): Sensor tag or sensor ID.
            app_timestamp (float, optional): Application timestamp.
            sensor_timestamp (float, optional): Sensor timestamp.
            accuracy (int, optional): Sensor accuracy.
        """
        self.tag = tag
        self.app_timestamp = app_timestamp
        self.sensor_timestamp = sensor_timestamp
        self.accuracy = accuracy

    @abstractmethod
    def export_row(self, index, include_calculated=False):
        """
        Export sensor data as a row for a CSV file.

        This method should be implemented by subclasses to format
        sensor data for CSV export.

        Args:
            index (int): The row index in the CSV file.
            include_calculated (bool): Whether to include calculated values in the output.

        Returns:
            str: A formatted string representing a row in the CSV file.
        """
        pass