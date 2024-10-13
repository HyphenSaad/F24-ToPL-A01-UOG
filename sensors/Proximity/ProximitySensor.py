from ..Base.SensorBase import SensorBase
from .ProximityCalculator import ProximityCalculator

class ProximitySensor(SensorBase):
    """
    A class to represent a Proximity Sensor.

    This class inherits from SensorBase and is used to store and process
    proximity sensor data.

    Attributes:
        prox (float): Proximity value.

    Inherited Attributes:
        tag (str): Sensor tag or sensor ID to identify sensor type.
        app_timestamp (float): Application timestamp.
        sensor_timestamp (float): Sensor timestamp.
        accuracy (int): Sensor accuracy.

    Methods:
        export_row(index, include_calculated): Export proximity data as a row for CSV file.
        get_headers(include_calculated): Get the headers for the CSV file.
    """

    def __init__(self, app_timestamp, sensor_timestamp, prox, accuracy):
        """
        Initialize the ProximitySensor object.

        Args:
            app_timestamp (float): Application timestamp.
            sensor_timestamp (float): Sensor timestamp.
            prox (float): Proximity value.
            accuracy (int): Sensor accuracy.
        """
        super().__init__('PROX', float(app_timestamp), float(sensor_timestamp), int(accuracy))
        self.prox = float(prox)
    
    def export_row(self, index, include_calculated=True):
        """
        Export proximity data as a row for a CSV file.

        Args:
            index (int): The row index.
            include_calculated (bool): Whether to include the calculated value in the output.

        Returns:
            str: A comma-separated string containing the index, proximity value, and optionally the calculated value.
        """
        base_row = f'{index},{self.prox}'
        if include_calculated:
            double_prox = ProximityCalculator.calculate_double_proximity(self.prox)
            return f'{base_row},{double_prox}'
        return base_row
    
    @staticmethod
    def get_headers(include_calculated=False):
        """
        Get the headers for the CSV file.

        Args:
            include_calculated (bool): Whether to include the header for the calculated value.

        Returns:
            str: A comma-separated string of header names.
        """
        return 'index,prox' + (',double_of_prox' if include_calculated else '')